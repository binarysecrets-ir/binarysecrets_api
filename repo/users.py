from sqlalchemy import select
from sqlalchemy.orm import Session

from models.user import User


def get_user_by_username(
    db: Session,
    username: str,
) -> User | None:
    stmt = select(User).where(
        User.username == username
    )
    return db.scalar(stmt)

def get_user_by_id(
    db: Session,
    id: int
) -> User | None:
    stmt = select(User).where(
        User.id == id
    )
    return db.scalar(stmt)


def get_user_by_email(
    db: Session,
    email: str,
) -> User | None:
    stmt = select(User).where(
        User.email == email
    )
    return db.scalar(stmt)


def create_user(
    db: Session,
    username: str,
    email: str,
    password_hash: str,
) -> User:

    user = User(
        username=username,
        email=email,
        password_hash=password_hash,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user