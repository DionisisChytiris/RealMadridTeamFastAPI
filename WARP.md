# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

Project: RealMadridFastAPI (FastAPI backend with MongoDB)

Common commands
- Install deps
  - pip install -r requirements.txt
- Run locally (auto-reload)
  - uvicorn main:app --reload
or  - python -m uvicorn main:app --reload
- Docker
  - docker build -t realmadrid-fastapi -f .Dockerfile .
  - docker run -p 8000:8000 realmadrid-fastapi
- Linting
  - No linter configured in this repo.
- Tests
  - No test suite present in this repo.

High-level architecture
- Entry point: main.py
  - Creates FastAPI app and an APIRouter mounted at prefix /players.
  - CORS middleware allows https://real-madrid-website.vercel.app and http://localhost:5173.
  - Routes (under /players):
    - GET / → fetches all documents via configuration.collection.find() and serializes with database.schemas.all_players.
    - POST / → inserts a player document from database.models.Team (Pydantic) into MongoDB.
    - PUT /{player_id} → updates a document by ObjectId, returns success message if found.
    - DELETE /{player_id} → deletes by ObjectId, returns success message if found.
  - Root route GET / returns a simple health/info message.
- Data models and serialization
  - database/models.py → Team(BaseModel) defines the player payload (position, number, firstname, surname, optional fields like type, placebirth, datebirth, weight, height, img).
  - database/schemas.py → individual_data() maps MongoDB documents to API shape (stringifies _id to id, includes img). all_players() aggregates over a cursor. Note: all_players is defined twice with equivalent behavior.
- Database configuration
  - configuration.py → Initializes a MongoClient, selects db team_db and collection team_data. The MongoDB connection URI is defined here.
- Deployment
  - .Dockerfile → Python 3.9-slim image, installs requirements, copies app, and runs uvicorn on port 8000.
  - vercel.json → Configures Vercel to build and route requests to main.py using @vercel/python.

Additional notes
- MongoDB ObjectId is expected in update/delete routes; invalid or non-existent ids return 404.
- If the MongoDB connection is not reachable, CRUD routes will fail at runtime.
