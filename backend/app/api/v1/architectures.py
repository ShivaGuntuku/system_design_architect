from uuid import UUID

from app.api.dependencies import get_db
from app.schemas.architecture import ArchitectureCreate, ArchitectureRead
from app.services.architecture_service import ArchitectureService
from app.schemas.component import ComponentCreate, ComponentRead
from app.services.component_service import ComponentService
from app.services.connection_service import ConnectionService
from app.schemas.connection import ConnectionCreate, ConnectionRead

from fastapi import APIRouter, Depends
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


@router.post("/{architecture_id}/components", response_model=ComponentRead, status_code=201)
def create_componet(architecture_id: UUID, payload: ComponentCreate, db: Session = Depends(get_db)):
    return ComponentService.create_component(architecture_id= UUID, db=db, payload=payload)
    

@router.get("/{architecture_id}/components", response_model=list[ComponentRead])
def list_components(architecture_id: UUID, db: Session = Depends(get_db)):
    return ComponentService.list_components(db)


@router.post("/{architecture_id}/connections", response_model=ConnectionRead, status_code=201)
def create_connection(payload: ConnectionCreate, db: Session = Depends(get_db)):
    return ConnectionService.create_connection(db=db, payload=payload)
    

@router.get("/{architecture_id}/connections", response_model=list[ConnectionRead])
def list_connections(db: Session = Depends(get_db)):
    return ComponentService.list_components(db)

@router.get("/{architecture_id}/graph")
def build_graph():
    pass