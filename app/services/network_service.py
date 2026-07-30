from fastapi import APIRouter, HTTPException
from app.services.network_service import network_service
from app.schemas.network_schema import NetworkSummary

router = APIRouter(
    prefix="/api/network",
    tags=["Network Planning"],  
)


@router.get("/summary", response_model=NetworkSummary)
async def summary():
    return network_service.get_summary()