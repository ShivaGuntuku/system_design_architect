from sqlalchemy.orm import Session
from uuid import UUID
from fastapi import HTTPException
from app.models.connections import Connection
from starlette import status


class ConnectionRepository:
    @staticmethod
    def create(db: Session, connection: Connection) -> Connection:

        db.add(connection)
        db.commit()
        db.refresh(connection)

        return connection

    @staticmethod
    def list_by_architecture(db: Session, architecture_id: UUID):
        return (
            db.query(Connection)
            .filter(Connection.architecture_id == architecture_id)
        )

    @staticmethod
    def get_existing_connection(
        db: Session,
        architecture_id: UUID,
        source_component_id: UUID,
        target_component_id: UUID,
    ):
        return (
            db.query(Connection)
            .filter(
                Connection.architecture_id == architecture_id,
                Connection.source_component_id == source_component_id,
                Connection.target_component_id == target_component_id,
            )
            .first()
        )

    @staticmethod
    def get_by_id(db: Session, connection_id: UUID) -> Connection | None:
        return db.get(Connection, connection_id)

    @staticmethod
    def delete(db: Session, connection_id: UUID) -> Connection | None:
        connection = db.get(Connection, connection_id)
        if not connection:
            return None
        db.delete(connection)
        db.commit()

        return connection
