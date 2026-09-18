from fastapi import APIRouter
from app.schemas.whatif_schemas import WhatIfRequest
from app.services.whatif_service import calculate_what_if

router = APIRouter(
    prefix="/what-if",
    tags=["What-if Analysis"]
)


@router.post("/what-if")
def what_if_analysis(request: WhatIfRequest):

    return calculate_what_if(request)