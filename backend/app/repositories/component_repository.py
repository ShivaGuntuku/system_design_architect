from sqlalchemy.orm import Session
from uuid import UUID
from app.models.components import Component


class ComponentRepository:
    @staticmethod
    def create(db: Session, component: Component) -> Component:

        db.add(component)
        db.commit()
        db.refresh(component)

        return component

    @staticmethod
    def get_by_id(db: Session, component_id: UUID) -> Component | None:
        return db.get(Component, component_id)

    @staticmethod
    def get_by_name(db: Session, architecture_id: UUID, name: str):
        return (
            db.query(Component)
            .filter(
                Component.architecture_id == architecture_id, Component.name == name
            )
            .first()
        )

    @staticmethod
    def list_by_architecture(db: Session, architecture_id: UUID) -> Component | None:
        return db.query(Component).filter(Component.architecture_id == architecture_id)

    @staticmethod
    def delete(db: Session, component_id: UUID):
        pass

    @staticmethod
    def exists(db: Session, component_id: UUID) -> bool:
        pass

    @staticmethod
    def update_position(
        db: Session,
        component_id: UUID,
        x: float,
        y: float,
    ):
        component = db.get(Component, component_id)

        component.x_position = x
        component.y_position = y

        db.add(component)
        db.commit()
        db.refresh(component)

        return component
