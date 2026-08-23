from fastapi import APIRouter
from app.schemas.whatif_schemas import WhatIfRequest

router = APIRouter(
    prefix="/network",
    tags=["Network Planning"]
)


@router.post("/what-if")
def what_if_analysis(request: WhatIfRequest):

    return {
        "message": "What-if analysis received",
        "scenario": request
    }