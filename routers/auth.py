from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from utils import create_access_token
from utils import verify_password, hash_password
from database.connection import get_db
from repo.users import (
    get_user_by_username,
    create_user,
    get_user_by_email, User
    )
from configs.user import (
    UserLogin,
    UserOut,
    UserCreate,
    UsernameUpdate
    )
from utils.security.dependencies import get_current_user




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


@router.patch("/username")
def change_username(
    data: UsernameUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    existing_user = get_user_by_username(
        db,
        data.new_username,
    )

    if existing_user and existing_user.id != current_user.id:
        raise HTTPException(
            status_code=409,
            detail="Username already exists",
        )

    current_user.username = data.new_username

    db.commit()
    db.refresh(current_user)

    return {
        "message": "Username updated successfully",
        "username": current_user.username,
    }
