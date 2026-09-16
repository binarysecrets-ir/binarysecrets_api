from fastapi.routing import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from repo.api import get_all_apis
from repo.api import create_api
from database import get_db
from configs.api import APICreate


router = APIRouter(
    prefix="/get_data",
    tags=["data_server"],
)


@router.get("/apis")
def get_api(
    db: Session = Depends(get_db),
):
    return get_all_apis(db)


@router.post("/api")
def create_new_api(
    data: APICreate,
    db: Session = Depends(get_db),
):
    return create_api(
        db=db,
        name=data.name,
        slug=data.slug,
        description=data.description,
        supported_formats=data.supported_formats,
        end_point=data.end_point,
        method=data.method,
        response=data.response,
        auth_method=data.auth_method,
    )