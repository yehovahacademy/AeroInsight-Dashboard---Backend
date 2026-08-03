from fastapi import APIRouter

from app.services.airport_intelligence_service import airport_intelligence_service
from app.schemas.airport_intelligence_schema import AirportIntelligenceResponse

router = APIRouter(prefix="/analytics", tags=["Airport Intelligence"])


@router.get(
    "/airport/{iata}",
    response_model=AirportIntelligenceResponse
)
async def analyze_airport(iata: str):
    return await airport_intelligence_service.analyze_airport(iata)