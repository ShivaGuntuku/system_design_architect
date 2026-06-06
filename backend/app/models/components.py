from uuid import UUID
from datetime import datetime
from sqlmodel import Field, Column, Relationship
from sqlalchemy import JSON, DateTime
from sqlalchemy.sql import func
from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.architecture import Architecture
    from app.models.connections import Connection

from .base import Base

COMPONENT_TYPES = [
    "load_balancer",
    "api_service",
    "worker",
    "redis",
    "postgres",
    "mongodb",
    "kafka",
    "queue",
    "cdn",
    "api_gateway",
]


class Component(Base, table=True):
    __tablename__ = "components"

    architecture_id: UUID = Field(foreign_key="architectures.id")
    name: str = Field(index=True)
    component_type: str
    config: Dict[str, Any] = Field(default_factory=dict, sa_column=Column(JSON))
    x_position: float = Field(default=100)
    y_position: float = Field(default=100)
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

    architecture: Optional["Architecture"] = Relationship(back_populates="components")
    outgoing_connections: list["Connection"] = Relationship(
        back_populates="source_component",
        sa_relationship_kwargs={"foreign_keys": "[Connection.source_component_id]"},
    )
    incoming_connections: list["Connection"] = Relationship(
        back_populates="target_component",
        sa_relationship_kwargs={"foreign_keys": "[Connection.target_component_id]"},
    )
