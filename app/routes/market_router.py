from fastapi import APIRouter, HTTPException

from app.services.market_service import market_service


router = APIRouter(
    tags=["Markets"],
)


@router.get("/")
async def get_all_markets():
    markets = market_service.get_all_markets()

    return {
        "count": len(markets),
        "markets": markets,
    }


@router.get("/from/{origin}")
async def get_markets_from_origin(origin: str):
    markets = market_service.get_market_from_origin(origin)

    return {
        "count": len(markets),
        "markets": markets,
    }


@router.get("/to/{destination}")
async def get_markets_to_destination(destination: str):
    markets = market_service.get_market_to_destination(destination)

    return {
        "count": len(markets),
        "markets": markets,
    }


@router.get("/{origin}/{destination}")
async def get_market(origin: str, destination: str):
    market = market_service.get_market(origin, destination)

    if market is None:
        raise HTTPException(
            status_code=404,
            detail="Market not found",
        )

    return market


@router.get("/{market_id}")
async def get_market_by_id(market_id: str):
    market = market_service.get_market_by_id(market_id)

    if market is None:
        raise HTTPException(
            status_code=404,
            detail="Market not found",
        )

    return market