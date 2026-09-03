from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.airports import router as airports_router
from app.routes.health import router as health_router
from app.routes import route_analyze

from app.routes.demand_forecast import router as demand_forecast_router
from app.repositories.market_repository import market_repository
from app.routes.market_router import router as market_router
from app.routes.whatif import router as whatif_router


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


app.include_router(whatif_router, prefix="/network", tags=["Network Planning"])
app.include_router(market_router, prefix="/markets", tags=["Markets"])


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




