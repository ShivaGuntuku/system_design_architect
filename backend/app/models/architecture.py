from typing import Optional, TYPE_CHECKING
from datetime import datetime

from sqlmodel import Field, Relationship
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func

from .base import Base

if TYPE_CHECKING:
    from .components import Component
    from .connections import Connection

class Architecture(Base,  table=True):
    __tablename__ = "architectures"

    name: str = Field(index=True, unique=True)

    description: Optional[str] = None

    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )

    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
        )
    )

    components: list["Component"] = Relationship(back_populates="architecture")
    connections: list["Connection"] = Relationship(back_populates="architecture")

