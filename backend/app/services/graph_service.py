

from click import UUID
from sqlmodel import Session


class GraphService:
    @staticmethod
    def build_graph(db: Session, architecture_id: UUID):
        pass