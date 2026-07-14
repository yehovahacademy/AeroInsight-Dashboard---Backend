from fastapi import FastAPI
from app.routes.airlines import router as airline_router
from app.routes.flights import router as flight_router
from app.routes.analytics import router as analytics_router

app = FastAPI(
title="My FastAPI Application"
)

app.include_router(airline_router, prefix="/airlines", tags=["Airlines"])

app.include_router(
    flight_router,
    prefix="/flights",
    tags=["Flights"]
)

app.include_router(
    analytics_router,
    prefix="/analytics",
    tags=["Analytics"]
)

