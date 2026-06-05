from uuid import UUID

from pydantic import BaseModel

from app.schemas.architecture import ArchitectureRead
from app.schemas.component import ComponentRead
from app.schemas.connection import ConnectionRead

class GraphStats(BaseModel):
    total_components: int
    total_connections: int

class GraphResponse(BaseModel):
    architecture: ArchitectureRead
    components: list[ComponentRead]
    connections: list[ConnectionRead]
    stats: GraphStats

class ArchitectureGraph(BaseModel):
    architecture: ArchitectureRead
    components: list[ComponentRead]
    connections: list[ConnectionRead]