from fastapi import APIRouter

from app.clients.api_ninjas_client import ApiNinjasClient

router = APIRouter()

client = ApiNinjasClient()


@router.get("/test-airports")
async def test_airports():
    return await client.get_airports("Mumbai")