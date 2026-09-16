from sqlalchemy import select
from sqlalchemy.orm import Session

from models import API


def get_all_apis(
    db: Session,
):
    stmt = select(API)
    return db.scalars(stmt).all()


def create_api(
    db: Session,
    name: str,
    slug: str,
    description: str,
    supported_formats: list[str],
    end_point: str,
    method: str,
    response: str,
    auth_method: str,
)-> API:
    api = API(
        name=name,
        slug=slug,
        description=description,
        supported_formats=supported_formats,
        end_point=end_point,
        method=method,
        response=response,
        auth_method=auth_method,
    )

    db.add(api)
    db.commit()
    db.refresh(api)

    return api