from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.components import Component
from app.schemas.component import ComponentCreate
from app.repositories.component_repository import ComponentRepository
from app.repositories.architecture_repository import ArchitectureRepository

from uuid import UUID

class ComponentService:
    @staticmethod
    def create_component(db: Session, payload: ComponentCreate, architecture_id:UUID) -> Component:
        architecture = (ArchitectureRepository.get_by_id(db, architecture_id=architecture_id))

        if not architecture:
            raise HTTPException(status_code=404, detail= "Architecture not found")
        
        existing = ComponentRepository.get_by_name(db=db, name=payload.name, architecture_id=architecture_id)
        if existing:
            raise HTTPException(status_code=400, detail="Component Already exists")
        component = Component(name=payload.name, 
                              component_type=payload.component_type,
                              config=payload.config,
                              architecture_id=architecture_id)
        return ComponentRepository.create(db=db, component=component)
    
    @staticmethod
    def list_components_by_architecture(db: Session,architecture_id: UUID):
        return ComponentRepository.list_by_architecture(db=db, architecture_id=architecture_id)
    

    def get_component():
        pass

    def delete_component():
        pass