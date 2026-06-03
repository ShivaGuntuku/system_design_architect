from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from sqlmodel import Field, SQLModel, Relationship
# from models.components import Component


class Base(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True)


class TimestampMixin(SQLModel):
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )

    updated_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
        )
    )


class Architecture(Base, TimestampMixin, table=True):
    __tablename__ = "architectures"

    name: str = Field(index=True, unique=True)

    description: Optional[str] = None

    # components: list["Component"] = Relationship(
    #     back_populates="architecture"
    # )
