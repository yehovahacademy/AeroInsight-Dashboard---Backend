from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from Database import get_db
from models.airport_model import Airport

app = FastAPI()


@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    airports = db.query(Airport).limit(5).all()

    return {
        "connected": True,
        "count": len(airports),
        "airports": [
            {
                "iata": airport.iata_code,
                "name": airport.airport_name,
                "city": airport.city
            }
            for airport in airports
        ]
    }