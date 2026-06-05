from uuid import UUID
from datetime import datetime
from sqlmodel import Field, Relationship
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from typing import Optional, TYPE_CHECKING

from .base import Base

if TYPE_CHECKING:
    from .components import Component
    from .architecture import Architecture


class Connection(Base, table=True):
    __tablename__ = "connections"

    architecture_id: UUID = Field(foreign_key="architectures.id")
    source_component_id: UUID = Field(
        foreign_key="components.id",
    )
    target_component_id: UUID = Field(
        foreign_key="components.id",
    )

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

    architecture: Optional["Architecture"] = Relationship(back_populates="connections")
    source_component: Optional["Component"] = Relationship(
        back_populates="outgoing_connections",
        sa_relationship_kwargs={"foreign_keys": "[Connection.source_component_id]"},
    )
    target_component: Optional["Component"] = Relationship(
        back_populates="incoming_connections",
        sa_relationship_kwargs={"foreign_keys": "[Connection.target_component_id]"},
    )
