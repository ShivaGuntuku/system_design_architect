from uuid import UUID

from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.connections import Connection
from app.schemas.connection import ConnectionCreate
from app.repositories.connection_repository import ConnectionRepository
from app.repositories.component_repository import ComponentRepository
from app.repositories.architecture_repository import ArchitectureRepository


class ConnectionService:
    @staticmethod
    def create_connection(
        db: Session, architecture_id: UUID, payload: ConnectionCreate
    ) -> Connection:
        architecture = ArchitectureRepository.get_by_id(
            db, architecture_id=architecture_id
        )

        if not architecture:
            raise HTTPException(status_code=404, detail="Architecture not found")

        if payload.source_component_id == payload.target_component_id:
            raise HTTPException(
                status_code=400, detail="Self connections are not allowed"
            )
        source = ComponentRepository.get_by_id(
            db=db, component_id=payload.source_component_id
        )
        target = ComponentRepository.get_by_id(
            db=db, component_id=payload.target_component_id
        )
        if source.architecture_id != architecture_id:
            raise HTTPException(
                status_code=400,
                detail="Source component does not belong to architecture",
            )

        if target.architecture_id != architecture_id:
            raise HTTPException(
                status_code=400,
                detail="Target component does not belong to architecture",
            )
        existing = ConnectionRepository.get_existing_connection(
            db=db,
            architecture_id=architecture_id,
            source_component_id=payload.source_component_id,
            target_component_id=payload.target_component_id,
        )

        if existing:
            raise HTTPException(status_code=400, detail="Connection Already exists")

        connection = Connection(
            architecture_id=architecture_id,
            source_component_id=payload.source_component_id,
            target_component_id=payload.target_component_id,
        )
        return ConnectionRepository.create(db=db, connection=connection)

    @staticmethod
    def list_connections_by_architecture(db: Session, architecture_id: UUID):
        return ConnectionRepository.list_by_architecture(
            db=db, architecture_id=architecture_id
        )

    @staticmethod
    def delete_connection(db: Session, connection_id: UUID):
        connection = ConnectionRepository.delete(db=db, connection_id=connection_id)

        if not connection:
            raise HTTPException(status_code=404, detail="Connection not found")

        return connection
