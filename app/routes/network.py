from fastapi import APIRouter, HTTPException

from app.services.network_service import network_service

router = APIRouter(
    prefix="/api/network",
    tags=["Network Planning"],
)


