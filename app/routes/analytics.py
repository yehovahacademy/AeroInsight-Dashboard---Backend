from fastapi import APIRouter
from app.services.analytics_service import get_dashboard_stats
from app.schemas.analytics_schema import Analytics

router = APIRouter()

@router.get("/", response_model=Analytics)
def analytics():
    return get_dashboard_stats()