from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.routes.airlines import router as airline_router
from app.routes.flights import router as flight_router
from app.routes.analytics import router as analytics_router

from app.routes import weather


app = FastAPI(
title="My FastAPI Application"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://aero-insight-dashboard-frontend.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

app.include_router(
    weather.router,
    prefix="/weather",
    tags=["Weather"]
)

