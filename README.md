# ✈️ AeroInsight — Backend

> **FastAPI backend for the AeroInsight Aviation Intelligence & Network Planning Platform**

The **AeroInsight Backend** is the Python-based API and data-processing layer powering the AeroInsight aviation intelligence platform.

It provides REST APIs for airport intelligence, network planning, route analysis, fleet intelligence, weather information, forecasting, and aviation data processing.

The backend is built with **FastAPI and PostgreSQL**, with additional integrations for aviation and weather data.

---

## 🚀 Project Status

**Active Development**

The backend has evolved alongside the AeroInsight frontend and currently provides the foundation for:

* 🛫 Airport Intelligence
* 🌐 Network Planning
* 🛣️ Route Analysis
* ✈️ Fleet Intelligence
* 🌦️ Aviation Weather Intelligence
* 📈 Demand Forecasting
* 📊 Aviation Analytics
* 🗄️ PostgreSQL-backed aviation data
* 🔌 External API integrations

The architecture is being progressively refined as AeroInsight moves toward a more advanced aviation network planning platform.

---

## 🎯 Purpose

The backend is responsible for transforming aviation data and external information into structured APIs that can be consumed by the AeroInsight React frontend.

Its responsibilities include:

* Serving aviation data
* Querying PostgreSQL
* Processing airport information
* Performing route calculations
* Processing weather information
* Calculating aviation risk indicators
* Supporting network planning
* Providing fleet information
* Preparing analytical data
* Managing external API integrations

The backend intentionally keeps database operations and business logic separate from the frontend.

---

## 🧩 Backend Architecture

AeroInsight follows a layered backend architecture.

```text
                    React Frontend
                          │
                          │ REST API
                          ▼
                  ┌───────────────┐
                  │    FastAPI    │
                  │    Routers    │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │   Services    │
                  │ Business Logic│
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │ Repositories  │
                  │ Data Access   │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │  PostgreSQL   │
                  └───────────────┘
```

External aviation and weather APIs can also be accessed through dedicated services/clients.

---

## 💻 Technology Stack

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn
* HTTPX
* psycopg2

### Database

* PostgreSQL
* pgAdmin

### Data Processing

* Pandas
* NumPy
* Python aviation datasets

### External Data

The backend has worked with aviation and weather sources including:

* Open-Meteo
* METAR
* TAF
* SIGMET
* API Ninjas aviation APIs
* Aviation datasets

### Deployment

* Render
* GitHub

---

# 🛫 Core Backend Modules

## Airport Intelligence

The airport service provides structured airport lookup and search functionality.

Current operations include:

* IATA lookup
* ICAO lookup
* Airport search
* Airport metadata
* Geographic coordinates
* Airport information retrieval

The airport functionality follows the repository/service pattern:

```text
Airport Router
      ↓
Airport Loader
      ↓
Airport Repository
      ↓
PostgreSQL
```

This keeps API routing separate from database access.

---

## 🌐 Network Planning

Network Planning is the primary direction of the AeroInsight backend.

The backend supports the processing required by the Network Planner, including:

* Origin/destination airports
* Route analysis
* Distance calculations
* Aircraft selection
* Flights-per-day parameters
* Seasonal parameters
* Demand forecasting
* Weather considerations

The long-term objective is to provide increasingly sophisticated network planning intelligence.

---

## 🛣️ Route Analysis

Route analysis combines airport and operational information to evaluate potential routes.

The backend has been developed to support information such as:

* Origin airport
* Destination airport
* Distance
* Aircraft
* Flight frequency
* Seasonal considerations
* Demand
* Weather risk

This provides the foundation for future route profitability and optimization features.

---

## 🌦️ Aviation Weather Intelligence

Weather intelligence is an important part of AeroInsight's operational analysis.

The backend processes aviation weather information including:

### METAR

Used for current airport weather conditions.

### TAF

Used for airport weather forecasts.

### SIGMET

Used to identify significant aviation weather hazards.

The backend also integrates Open-Meteo data for weather forecasting and additional weather information.

Weather data can be transformed into risk indicators for use by the Network Planner.

---

## ✈️ Fleet Intelligence

The backend supports fleet-related information used by the AeroInsight dashboard.

Aircraft information has been sourced from aviation datasets and processed for analytical use.

Current aircraft categories used in the Network Planner include:

```text
A320
A321neo
B737 MAX
B777
ATR 72
```

Fleet-related analytics include information such as:

* Aircraft count
* Manufacturers
* Aircraft types
* Fleet statistics

---

# 🗄️ PostgreSQL Database

PostgreSQL is the primary relational database for AeroInsight.

The database is used for structured aviation information including airport and other aviation datasets.

The project previously worked extensively with large CSV datasets.

Because some datasets were too large to efficiently maintain inside Git, PostgreSQL became the primary approach for storing and querying the data.

Database administration and development have been performed using **pgAdmin**.

---

## 📊 Aviation Datasets

The backend has worked with datasets including:

```text
airports.dat
routes.dat
countries.dat
planes.dat
```

These datasets provide information used throughout the AeroInsight platform.

The backend processes and exposes the relevant information through APIs instead of requiring the frontend to directly handle raw datasets.

---

# 🔌 API Design

The backend exposes REST endpoints through FastAPI routers.

An example airport API structure is:

```text
GET /api/airports/search/{query}
GET /api/airports/{airport_code}
```

Other API areas include functionality related to:

```text
Airport Intelligence
Network Planning
Route Analysis
Fleet Intelligence
Weather
Analytics
```

The exact endpoint structure continues to evolve during development.

---

# 🧱 Repository Pattern

Database operations are isolated inside repository classes.

For example:

```text
FastAPI Router
      ↓
Service / Loader
      ↓
Repository
      ↓
PostgreSQL
```

This architecture provides several benefits:

* Cleaner API routers
* Separation of concerns
* Easier database testing
* Reusable data-access logic
* Easier future database changes
* Better maintainability

---

# 📦 Project Structure

The backend structure follows a modular architecture similar to:

```text
AeroInsight-Backend/
│
├── app/
│   │
│   ├── routers/
│   │
│   ├── services/
│   │
│   ├── repositories/
│   │
│   ├── schemas/
│   │
│   ├── clients/
│   │
│   ├── database/
│   │
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

The exact structure continues to evolve as new backend modules are introduced.

---

# ⚙️ Environment Variables

Production credentials and API keys are stored through environment variables rather than being committed to the repository.

Typical configuration includes:

```env
DATABASE_URL=
API_NINJAS_KEY=
AEROAPI_KEY=
```

The application reads configuration from the environment.

For local development, environment variables can be configured through a `.env` file.

**Never commit database credentials or API keys to GitHub.**

---

# 🛠️ Local Development

## 1. Clone the repository

```bash
git clone https://github.com/<your-username>/AeroInsight-Backend.git
cd AeroInsight-Backend
```

## 2. Create a virtual environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file and configure the required database/API settings.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/AeroInsight
```

---

## 5. Start FastAPI

```bash
uvicorn app.main:app --reload
```

The development server will normally run at:

```text
http://127.0.0.1:8000
```

FastAPI automatically provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

and:

```text
http://127.0.0.1:8000/redoc
```

---

# ☁️ Production Deployment

The AeroInsight backend is deployed using **Render**.

The deployment architecture is:

```text
GitHub
   │
   ▼
Render
   │
   ├── FastAPI Backend
   │
   └── PostgreSQL Database
```

The backend uses environment variables for production database configuration and external API credentials.

---

# 🔐 Security

The backend follows environment-based configuration for sensitive values.

Sensitive information such as:

* Database passwords
* API keys
* Authentication credentials
* Production connection strings

should never be committed to the repository.

The `.gitignore` should include local environment files such as:

```text
.env
.venv/
__pycache__/
```

---

# 🌍 Frontend Integration

The backend is designed to serve the separate AeroInsight React frontend.

```text
┌──────────────────────────┐
│   AeroInsight Frontend   │
│      React + Vite        │
└────────────┬─────────────┘
             │
             │ REST API
             ▼
┌──────────────────────────┐
│   AeroInsight Backend    │
│         FastAPI          │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│       PostgreSQL         │
└──────────────────────────┘
```

CORS is configured so that the deployed frontend can communicate with the deployed backend.

---

# 🧠 Engineering Focus

The backend is being developed as a practical exploration of:

* FastAPI
* REST API architecture
* PostgreSQL
* Repository patterns
* Service-layer architecture
* Pydantic schemas
* Async HTTP requests
* External API integration
* Aviation data processing
* Weather intelligence
* Data analytics
* Forecasting
* Cloud deployment
* Production debugging

The architecture is intentionally being built in a modular manner so additional aviation intelligence modules can be added without tightly coupling them to the existing system.

---

# 🗺️ Roadmap

Planned backend improvements include:

* [ ] Advanced route profitability calculations
* [ ] Historical route analysis
* [ ] What-if network analysis
* [ ] Improved demand forecasting
* [ ] Route optimization algorithms
* [ ] Additional weather risk models
* [ ] Expanded fleet analytics
* [ ] Network connectivity analysis
* [ ] Additional airport intelligence
* [ ] Airline-specific analytics
* [ ] Improved API validation
* [ ] Automated backend testing
* [ ] Production monitoring
* [ ] Improved error handling

The roadmap will evolve as the AeroInsight platform develops.

---

# 📈 Development Journey

The AeroInsight backend has gone through several architectural iterations.

The development process has included:

1. Initial aviation API experimentation
2. Airport data processing
3. FastAPI API development
4. Aviation dataset integration
5. PostgreSQL database implementation
6. Repository/service architecture
7. External weather API integration
8. METAR/TAF processing
9. SIGMET processing
10. Fleet intelligence
11. Network Planning APIs
12. Demand forecasting
13. Render deployment
14. Production database integration
15. API and CORS debugging
16. Continued backend architecture refinement

This iterative approach allows the backend to grow alongside the AeroInsight frontend and product vision.

---

# 👨‍💻 Author

**Joshua Joseph**

Junior Python Developer & AI Researcher

AeroInsight is a portfolio and research-oriented project combining:

**Aviation × Python × FastAPI × Data × AI**

---

# ⭐ AeroInsight Backend

> **Building the intelligence layer behind aviation network planning.**
