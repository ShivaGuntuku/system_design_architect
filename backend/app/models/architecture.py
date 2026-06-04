
from typing import Optional
from uuid import UUID, uuid4


from sqlmodel import Field, SQLModel, Relationship
from base import TimestampMixin
from .components import Component
from .connections import Connection


class Base(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True)


class Architecture(Base, TimestampMixin, table=True):
    __tablename__ = "architectures"

    name: str = Field(index=True, unique=True)

    description: Optional[str] = None

    components: list["Component"] = Relationship(
        back_populates="architecture"
    )
    connections: list["Connection"] = Relationship(
        back_populates="architecture"
    )