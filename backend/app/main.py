from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.v1.architectures import router as architecture_router

app = FastAPI(
    title="System Design Playground"
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

