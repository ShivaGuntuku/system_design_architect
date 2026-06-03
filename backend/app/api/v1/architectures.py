from uuid import UUID

from app.api.dependencies import get_db
from app.schemas.architecture import ArchitectureCreate, ArchitectureRead
from app.services.architecture_service import ArchitectureService
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/architectures", tags=["Architectures"])


@router.post("", response_model=ArchitectureRead, status_code=201)
def create_architecture(payload: ArchitectureCreate, db: Session = Depends(get_db)):
    return ArchitectureService.create_architecture(db=db, payload=payload)


@router.get("/{architecture_id}", response_model=ArchitectureRead)
def get_architecture(architecture_id: UUID, db: Session = Depends(get_db)):
    return ArchitectureService.get_architecture(db=db, architecture_id=architecture_id)


@router.get("",response_model=list[ArchitectureRead])
def list_architectures(db:Session = Depends(get_db)):
    return ArchitectureService.list_architecture(db)