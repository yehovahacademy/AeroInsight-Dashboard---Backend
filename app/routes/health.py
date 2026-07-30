from fastapi import APIRouter

router = APIRouter(
    prefix="/api/health",
    tags=["Health"],
)


@router.get("")
async def health():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "services": {
            "weather": True,
            "network": True,
            "flights": False,
            "aeroapi": False,
        },
    }