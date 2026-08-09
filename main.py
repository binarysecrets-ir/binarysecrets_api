from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from utils.images import ImageProcessor
from models import (
    ImageConfig
)

# from pydantic import BaseModel, ConfigDict
from PIL import Image

app = FastAPI(docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/scalar")
async def scalar():
    """returns scalar docs"""
    html_content = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Scalar Offline API Reference</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>
      <body>
        <script id="api-reference" data-url="/openapi.json"></script>

        <script src="/static/standalone.js"></script>
      </body>
    </html>
    """
    return HTMLResponse(content=html_content)



@app.post("/image/compress")
async def image_compress(
    image: UploadFile,
    config: str = Form(...),
):
    config = ImageConfig.model_validate_json(config)

    processor = ImageProcessor(
        image=image,
        config=config,
    )

    result = processor.process()

    return StreamingResponse(
        result,
        media_type=f"image/{config.out_format.lower()}",
        headers={
            "Content-Disposition": "attachment; filename=compressed"
        },
    )