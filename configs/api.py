from pydantic import BaseModel, StringConstraints
from typing import Annotated, Literal

NameType = Annotated[str, StringConstraints(
    strip_whitespace=True,
    max_length=100
    )]

DescriptionType = Annotated[str,StringConstraints(
    strip_whitespace=True,
    max_length=255
)]

MethodType = Literal["POST", "GET"]

ResponseType = Literal["JSON", "IMAGE"]

AuthType = Literal["token", "password"]

class APICreate(BaseModel):
    name: NameType
    slug: str
    description: DescriptionType
    supported_formats: list
    end_point: str
    method: MethodType
    response: ResponseType
    auth_method: AuthType
