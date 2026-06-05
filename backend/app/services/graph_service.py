from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.architecture_repository import ArchitectureRepository

from app.repositories.component_repository import ComponentRepository

from app.repositories.connection_repository import ConnectionRepository

from app.schemas.graph import GraphResponse, GraphStats
from app.services.graph_validator import GraphValidator


class GraphService:
    @staticmethod
    def build_graph(db: Session, architecture_id: UUID) -> GraphResponse:

        architecture = ArchitectureRepository.get_by_id(
            db=db, architecture_id=architecture_id
        )

        if not architecture:
            raise HTTPException(status_code=404, detail="Architecture not found")

        components = ComponentRepository.list_by_architecture(
            db=db, architecture_id=architecture_id
        )

        connections = ConnectionRepository.list_by_architecture(
            db=db, architecture_id=architecture_id
        )

        stats = GraphStats(
            total_components=len(list(components)),
            total_connections=len(list(connections)),
        )
        return GraphResponse(
            architecture=architecture,
            components=components,
            connections=connections,
            stats=stats,
        )

    @staticmethod
    def validate_graph(db: Session, architecture_id: UUID) -> GraphResponse:
        graph = GraphService.build_graph(db, architecture_id=architecture_id)

        return GraphValidator.validate(graph=graph)
