from uuid import UUID
from sqlmodel import Field, Column, Relationship
from sqlalchemy import JSON
from typing import Any, Dict, Optional

from models.architecture import Base, Architecture, TimestampMixin
from .connections import Connection

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
    "api_gateway"
]

class Component(Base, TimestampMixin, table=True):
    __tablename__ = "components"
    
    architecture_id: UUID = Field(
        foreign_key="architectures.id"
    )
    name: str = Field(index=True)
    component_type: str 
    config: Dict[str, Any] = Field(
        default_factory=dict, sa_column=Column(JSON)
    )

    architecture: Optional["Architecture"] = Relationship(back_populates="components")
    outgoing_connections: list["Connection"] = Relationship(
        back_populates="source_component"
    )
    incoming_connections: list["Connection"] = Relationship(back_populates="target_component")