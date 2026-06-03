from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class ArchitectureCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Architecture name"
    )

    description: Optional[str] = Field(
        default=None,
        max_length=1000,
        description="Architecture description"
    )


class ArchitectureRead(BaseModel):
    id: UUID
    name: str
    description: Optional[str]

    created_at: datetime
    updated_at: Optional[datetime]

    model_config = {
        "from_attributes": True
    }


class ArchitectureUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None