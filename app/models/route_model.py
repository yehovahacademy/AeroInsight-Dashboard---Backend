from sqlalchemy import Column, Integer, String, Float
from database import Base


class Route(Base):
    __tablename__ = "routes"

    route_id = Column(Integer, primary_key=True)
    origin_iata = Column(String(3), nullable=False)
    destination_iata = Column(String(3), nullable=False)
    origin_latitude = Column(Float, nullable=False)
    origin_longitude = Column(Float, nullable=False)
    destination_latitude = Column(Float, nullable=False)
    destination_longitude = Column(Float, nullable=False)
    distance_km = Column(Float, nullable=False)
    region = Column(String(50))