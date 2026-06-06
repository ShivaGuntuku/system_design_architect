from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any, Literal

ComponentType = Literal[
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

class ComponentCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Component name"
    )
    component_type: ComponentType
    config: Dict[str, Any]

class ComponentRead(BaseModel):
    id: UUID
    name: str
    architecture_id: UUID
    component_type: str
    config: Dict[str, Any]
    created_at: datetime
    updated_at: Optional[datetime]
    x_position: float
    y_position: float
    model_config = {
        "from_attributes": True
    }

class ComponentUpdate(BaseModel):
    name: str | None = None
    config: dict | None = None

class PositionUpdate(BaseModel):
    x_position: float
    y_position: float