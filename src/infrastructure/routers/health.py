from typing import Any

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def healthcheck() -> dict[str, Any]:
    return {"status": "ok"}
