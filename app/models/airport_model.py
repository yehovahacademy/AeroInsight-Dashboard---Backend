from sqlalchemy import Column, Integer, String, Float
from Database import Base


class Airport(Base):
    __tablename__ = "airports"

    airport_id = Column(Integer, primary_key=True)
    iata_code = Column(String(3), unique=True, nullable=False)
    icao_code = Column(String(4), nullable=False)
    airport_name = Column(String(150), nullable=False)
    city = Column(String(100), nullable=False)
    state_ut = Column(String(100))
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    elevation_ft = Column(Integer)
    airport_type = Column(String(30), nullable=False)
    timezone = Column(String(20))