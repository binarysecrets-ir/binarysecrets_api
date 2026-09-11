from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from utils import create_access_token
from utils import verify_password, hash_password
from database.connection import get_db
from repo.users import (
    get_user_by_username,
    create_user,
    get_user_by_email
    )
from configs.user import (
    UserLogin,
    UserOut,
    UserCreate
    )




router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/signup", response_model=UserOut)
def signup(
    data: UserCreate,
    db: Session = Depends(get_db),
):
    if get_user_by_username(db, data.username):
        raise HTTPException(
            status_code=409,
            detail="Username already exists",
        )

    if get_user_by_email(db, data.email):
        raise HTTPException(
            status_code=409,
            detail="Email already exists",
        )

    user = create_user(
        db=db,
        username=data.username,
        email=data.email,
        password_hash=hash_password(data.password),
    )

    return user


@router.post("/login")
def login(
    data: UserLogin,
    db: Session = Depends(get_db),
):
    user = get_user_by_username(
        db,
        data.username,
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    if not verify_password(
        data.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="User is inactive",
        )

    access_token = create_access_token(
        {
            "sub": str(user.id),
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }