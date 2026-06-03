from fastapi import FastAPI

from .api.v1.architectures import router as architecture_router

app = FastAPI(
    title="System Design Playground"
)

app.include_router(
    architecture_router,
    prefix="/api/v1"
)

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

