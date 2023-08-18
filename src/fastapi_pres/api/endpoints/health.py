from fastapi import APIRouter, Response


router = APIRouter()


@router.get(
    "/health",
)
async def home():
    return Response(status_code=200)
