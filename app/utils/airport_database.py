"""
Airport Intelligence Database

This file contains static airport metadata used throughout
the application. In the future, this can be replaced by
a PostgreSQL database or an external aviation API.
"""

AIRPORTS = {
    "BOM": {
        "iata": "BOM",
        "icao": "VABB",
        "name": "Chhatrapati Shivaji Maharaj International Airport",
        "city": "Mumbai",
        "country": "India",
        "latitude": 19.0896,
        "longitude": 72.8656,
        "elevation_ft": 39,
        "timezone": "Asia/Kolkata",
        "airport_type": "International",
        "runways": 2,
    },

    "DEL": {
        "iata": "DEL",
        "icao": "VIDP",
        "name": "Indira Gandhi International Airport",
        "city": "New Delhi",
        "country": "India",
        "latitude": 28.5562,
        "longitude": 77.1000,
        "elevation_ft": 777,
        "timezone": "Asia/Kolkata",
        "airport_type": "International",
        "runways": 3,
    },

    "BLR": {
        "iata": "BLR",
        "icao": "VOBL",
        "name": "Kempegowda International Airport",
        "city": "Bengaluru",
        "country": "India",
        "latitude": 13.1986,
        "longitude": 77.7066,
        "elevation_ft": 3000,
        "timezone": "Asia/Kolkata",
        "airport_type": "International",
        "runways": 2,
    },

    "MAA": {
        "iata": "MAA",
        "icao": "VOMM",
        "name": "Chennai International Airport",
        "city": "Chennai",
        "country": "India",
        "latitude": 12.9900,
        "longitude": 80.1693,
        "elevation_ft": 52,
        "timezone": "Asia/Kolkata",
        "airport_type": "International",
        "runways": 2,
    },

    "HYD": {
        "iata": "HYD",
        "icao": "VOHS",
        "name": "Rajiv Gandhi International Airport",
        "city": "Hyderabad",
        "country": "India",
        "latitude": 17.2403,
        "longitude": 78.4294,
        "elevation_ft": 2024,
        "timezone": "Asia/Kolkata",
        "airport_type": "International",
        "runways": 2,
    },

    "CCU": {
        "iata": "CCU",
        "icao": "VECC",
        "name": "Netaji Subhas Chandra Bose International Airport",
        "city": "Kolkata",
        "country": "India",
        "latitude": 22.6547,
        "longitude": 88.4467,
        "elevation_ft": 16,
        "timezone": "Asia/Kolkata",
        "airport_type": "International",
        "runways": 2,
    },

    "GOI": {
        "iata": "GOI",
        "icao": "VOGO",
        "name": "Goa International Airport",
        "city": "Goa",
        "country": "India",
        "latitude": 15.3808,
        "longitude": 73.8314,
        "elevation_ft": 150,
        "timezone": "Asia/Kolkata",
        "airport_type": "International",
        "runways": 1,
    },

    "PNQ": {
        "iata": "PNQ",
        "icao": "VAPO",
        "name": "Pune Airport",
        "city": "Pune",
        "country": "India",
        "latitude": 18.5822,
        "longitude": 73.9197,
        "elevation_ft": 1942,
        "timezone": "Asia/Kolkata",
        "airport_type": "Domestic",
        "runways": 1,
    },

    "AMD": {
        "iata": "AMD",
        "icao": "VAAH",
        "name": "Sardar Vallabhbhai Patel International Airport",
        "city": "Ahmedabad",
        "country": "India",
        "latitude": 23.0772,
        "longitude": 72.6347,
        "elevation_ft": 189,
        "timezone": "Asia/Kolkata",
        "airport_type": "International",
        "runways": 1,
    },

    "COK": {
        "iata": "COK",
        "icao": "VOCI",
        "name": "Cochin International Airport",
        "city": "Kochi",
        "country": "India",
        "latitude": 10.1520,
        "longitude": 76.4019,
        "elevation_ft": 30,
        "timezone": "Asia/Kolkata",
        "airport_type": "International",
        "runways": 1,
    }
}