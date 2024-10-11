import uvicorn
from fastapi import FastAPI

from src.infrastructure.routers.mercadona import router as mercadona_router
from src.infrastructure.routers.health import router as health_router

app = FastAPI()

app.include_router(health_router, prefix="/health")
app.include_router(mercadona_router, prefix="/mercadona")

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
