from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.routes.airlines import router as airline_router
from app.routes.flights import router as flight_router
from app.routes.analytics import router as analytics_router
from app.routes.airports import router as airports_router
from app.routes.health import router as health_router
from app.routes import network
from app.routes.airport_intelligence import router as airport_router

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

app.include_router(
    airports_router,
    prefix="/airports",
    tags=["Airports"]
)

app.include_router(
    health_router,  
    prefix="/health",
    tags=["Health"]
)

app.include_router(
  network.router,
    prefix="/network",
    tags=["Network Planning"]
)

app.include_router(
    airport_router,
    prefix="/airport-intelligence",
    tags=["Airport Intelligence"]
)



