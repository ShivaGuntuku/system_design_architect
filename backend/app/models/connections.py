from uuid import UUID
from sqlmodel import Field, Relationship
from typing import Optional
from base import TimestampMixin
from architecture import Base, Architecture
from components import Component


class Connection(Base, TimestampMixin, table=True):
    __tablename__ = "connections"

    architecture_id: UUID = Field(foreign_key="architectures.id")
    source_component_id: UUID = Field(
        foreign_key="components.id",
        sa_relationship_kwargs={"foreign_keys": "[Connection.source_component_id]"},
    )
    target_component_id: UUID = Field(
        foreign_key="components.id",
        sa_relationship_kwargs={"foreign_keys": "[Connection.target_component_id]"},
    )

    architecture: Optional["Architecture"] = Relationship(back_populates="connections")
    source_component: Optional["Component"] = Relationship(
        back_populates="outgoing_connections",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    target_component: Optional["Component"] = Relationship(
        back_populates="incoming_connections",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
