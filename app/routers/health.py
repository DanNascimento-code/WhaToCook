from fastapi import APIRouter
from services.health_service import get_health_status

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)

@router.get("/health")
def health_check():
    response_model = get_health_status()
    return response_model
