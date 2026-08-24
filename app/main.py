from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.airports import router as airports_router
from app.routes.health import router as health_router
from app.routes import route_analyze

from app.routes.demand_forecast import router as demand_forecast_router
from app.repositories.route_repository import route_repository
from app.routes.router import router as route_router
from app.routes.whatif import router as whatif_router

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
        "https://aero-insight-dashboard-frontend.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(whatif_router, prefix="/network", tags=["Network Planning"])
app.include_router(route_router, prefix="/routes", tags=["Routes"])


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
  route_analyze.router,
  prefix ="/api/network",
    tags=["Network Planning"]
)


app.include_router(
    demand_forecast_router,
    prefix="/demand-forecast",
    tags=["Demand Forecast"]
)




