from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel
from sqlalchemy import Column, DateTime
from datetime import datetime
from sqlalchemy.sql import func


class Base(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True)


# def get_timestamp_fields():
#     """Factory function to create fresh timestamp fields for each model."""
#     return {
#         "created_at": Field(
#             default=None,
#             sa_column=Column(DateTime(timezone=True), server_default=func.now())
#         ),
#         "updated_at": Field(
#             default=None,
#             sa_column=Column(
#                 DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
#             )
#         ),
#     }


# class TimestampMixin:
#     """Mixin to add timestamp fields to models."""
#     created_at: Optional[datetime] = None
#     updated_at: Optional[datetime] = None
