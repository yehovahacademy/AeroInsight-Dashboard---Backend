from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.airlines import router as airline_router
from app.routes.analytics import router as analytics_router
from app.routes.airports import router as airports_router
from app.routes.health import router as health_router
from app.routes import network
from app.routes.airport_intelligence import router as airport_router
from app.routes.fleet import router as fleet_router
from app.routes.weather import router as metar_router
from app.routes.demand_forecast import router as demand_forecast_router

from app.routes import weather
from app.repositories.route_repository import route_repository







app = FastAPI(
    title="AeroInsight API",
    
)

@app.get("/test-routes")
def test_routes():
    routes = route_repository.get_all()

    return {
        "count": len(routes),
        "routes": routes[:5]
    }



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
  prefix ="/api/network",
    tags=["Network Planning"]
)

app.include_router(
    airport_router,
    prefix="/airport-intelligence",
    tags=["Airport Intelligence"]
)

app.include_router(
    fleet_router,
    prefix="/fleet",    
    tags=["Fleet"]
)

app.include_router(
    demand_forecast_router,
    prefix="/demand-forecast",
    tags=["Demand Forecast"]
)




