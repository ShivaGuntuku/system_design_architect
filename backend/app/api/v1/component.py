# app/api/v1/components.py
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.api.dependencies import get_db
from app.schemas.component import PositionUpdate
from app.services.component_service import ComponentService

router = APIRouter(
    prefix="/components",
    tags=["Components"]
)

@router.patch("/{component_id}/position")
def update_position(
    component_id: UUID,
    payload: PositionUpdate,
    db: Session = Depends(get_db),
):
    return ComponentService.update_position(
        db=db,
        component_id=component_id,
        x=payload.x_position,
        y=payload.y_position,
    )