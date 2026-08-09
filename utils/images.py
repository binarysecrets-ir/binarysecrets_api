from PIL import Image
from models import ImageConfig
from fastapi import HTTPException, UploadFile

from abc import ABC, abstractmethod
from io import BytesIO
from typing import Type

from PIL import Image

from models import ImageConfig


class ImageEncoder(ABC):

    @abstractmethod
    def encode(
        self,
        image: Image.Image,
        output: BytesIO,
        quality: int,
    ) -> None:
        ...


class JPEGEncoder(ImageEncoder):

    def encode(
        self,
        image: Image.Image,
        output: BytesIO,
        quality: int,
    ) -> None:

        if image.mode in ("RGBA", "LA", "P"):
            image = image.convert("RGB")

        image.save(
            output,
            format="JPEG",
            quality=quality,
            optimize=True,
        )


class PNGEncoder(ImageEncoder):

    def encode(
        self,
        image: Image.Image,
        output: BytesIO,
        quality: int,
    ) -> None:

        image.save(
            output,
            format="PNG",
            optimize=True,
        )


class AVIFEncoder(ImageEncoder):

    def encode(
        self,
        image: Image.Image,
        output: BytesIO,
        quality: int,
    ) -> None:

        image.save(
            output,
            format="AVIF",
            quality=quality,
        )


ENCODERS: dict[str, Type[ImageEncoder]] = {
    "JPEG": JPEGEncoder,
    "PNG": PNGEncoder,
    "AVIF": AVIFEncoder,
}

class ImageProcessor:

    def __init__(
        self,
        image:UploadFile,
        config: ImageConfig,
    ):
        self.image = image
        self.config = config

    def get_encoder(self) -> ImageEncoder:
        encoder_class = ENCODERS[self.config.out_format]

        return encoder_class()

    def validate(self):
        try:
            Image.open(self.image.file).verify()
            return True
        except:
            raise HTTPException(406, 'invalid image!')

    def resize(self, image: Image.Image) -> Image.Image:
        target = (
            self.config.width,
            self.config.height,
        )

        if image.size == target or target[0] == None:
            return image

        return image.resize(
            target,
            Image.Resampling.LANCZOS,
        )

    def compress(self, image: Image.Image) -> BytesIO:
        output = BytesIO()

        image = self.resize(image)

        encoder = self.get_encoder()

        encoder.encode(
            image=image,
            output=output,
            quality=self.config.quality,
        )

        output.seek(0)

        return output

    def open(self):
        return Image.open(self.image.file)

    def process(self) -> BytesIO:
        self.validate()

        image = self.open()

        return self.compress(image)
