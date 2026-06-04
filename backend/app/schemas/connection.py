from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ConnectionCreate(BaseModel):
    source_component_id: UUID
    target_component_id: UUID

class ConnectionRead(BaseModel):
    id: UUID
    source_component_id: UUID
    target_component_id: UUID
    created_at: datetime
    updated_at: Optional[datetime]

    model_config = {
        "from_attributes": True
    }

