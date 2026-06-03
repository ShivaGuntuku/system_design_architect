# app/services/architecture_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from uuid import UUID
from app.models.architecture import Architecture
from app.schemas.architecture import ArchitectureCreate
from app.repositories.architecture_repository import ArchitectureRepository


class ArchitectureService:
    @staticmethod
    def create_architecture(db: Session, payload: ArchitectureCreate) -> Architecture:

        existing = ArchitectureRepository.get_by_name(db=db, name=payload.name)
        if existing:
            raise HTTPException(status_code=400,
                                detail= "Architecture already exists")
        
        architecture = Architecture(name=payload.name, description=payload.description)

        return (ArchitectureRepository.create(db=db, architecture=architecture))

    @staticmethod
    def get_architecture(db: Session, architecture_id:UUID):
        architecture = (ArchitectureRepository.get_by_id(db, architecture_id=architecture_id))

        if not architecture:
            raise HTTPException(status_code=404, detail= "Architecture not found")
        
        return architecture
    
    @staticmethod
    def list_architecture(db:Session):
        return ArchitectureRepository.list_all(db)

    @staticmethod
    def validate_architecture(db, architecture_id):
        pass

    @staticmethod
    def analyze_architecture():
        pass

    @staticmethod
    def run_failure_scenario():
        pass

    @staticmethod
    def calculate_score():
        pass
