from typing import Annotated

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    StringConstraints,
)


UserNameType = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=3,
        max_length=50,
        strict=True,
    ),
]


PasswordType = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=8,
        max_length=128,
    ),
]


class UserCreate(BaseModel):
    username: UserNameType
    password: PasswordType
    email: EmailStr


class UserLogin(BaseModel):
    username: UserNameType
    password: PasswordType


class UserOut(BaseModel):
    id: int
    username: UserNameType
    email: EmailStr
    is_active: bool

    model_config = ConfigDict(from_attributes=True)