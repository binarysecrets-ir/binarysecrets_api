from pydantic import BaseModel, Field, ConfigDict, StringConstraints
from typing import Annotated, Literal

ImageFormat = Annotated[
    Literal["JPEG", "AVIF", "PNG"],
    StringConstraints(to_upper=True),
]

class ImageConfig(BaseModel):
    model_config = ConfigDict(frozen=True)

    quality: Annotated[int, Field(gt=0, lt=101, default=85)]
    height: Annotated[int | None, Field(gt=0, default=None)]
    width: Annotated[int | None, Field(gt=0, default=None)]

    out_format: ImageFormat
