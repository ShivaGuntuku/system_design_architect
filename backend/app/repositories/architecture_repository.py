from uuid import UUID

from sqlalchemy.orm import Session

from app.models.architecture import Architecture


class ArchitectureRepository:
    @staticmethod
    def create(db: Session, architecture: Architecture) -> Architecture:

        db.add(architecture)
        db.commit()
        db.refresh(architecture)

        return architecture

    @staticmethod
    def get_by_id(db: Session, architecture_id: UUID) -> Architecture | None:

        return db.get(Architecture, architecture_id)

    @staticmethod
    def get_by_name(db: Session, name: str) -> Architecture | None:

        return db.query(Architecture).filter(Architecture.name == name).first()

    @staticmethod
    def list_all(db: Session):
        return db.query(Architecture).order_by(Architecture.created_at.desc()).all()
