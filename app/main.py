from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.airports import router as airports_router
from app.routes import route_analyze

from app.routes.monthly_demand_router import router as monthly_demand_router
from app.routes.historical_traffic_router import router as historical_traffic_router

from app.routes.demand_forecast import router as demand_forecast_router
from app.repositories.market_repository import market_repository as market_router
from app.routes.market_router import router as market_router


from app.routes.monthly_capacity_router import router as monthly_capacity_router


from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



    



app = FastAPI(
    title="AeroInsight API",
    
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")




@app.get("/protected")
async def protected(token: str = Depends(oauth2_scheme)):
    return {
        "message": "You accessed a protected route",
        "token": token
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



app.include_router(market_router, prefix="/markets", tags=["Markets"])
app.include_router(monthly_demand_router, prefix="/monthly_demand", tags=["Monthly Demand"])
app.include_router(historical_traffic_router, prefix="/historical_traffic", tags=["Historical Traffic"])
app.include_router(monthly_capacity_router, prefix="/monthly_capacity", tags=["Monthly Capacity"])


app.include_router(
    airports_router,
    prefix="/airports",
    tags=["Airports"]
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




