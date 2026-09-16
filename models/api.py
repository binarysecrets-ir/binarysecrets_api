from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, String, Text, func, JSON
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base

def utc_now():
    return datetime.now(timezone.utc)

class API(Base):
    __tablename__ = "apis"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    supported_formats: Mapped[list[str]] = mapped_column(
        JSON,
        nullable=False,
    )

    end_point: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    method: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    response: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    auth_method: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        onupdate=utc_now,
        nullable=False,
    )