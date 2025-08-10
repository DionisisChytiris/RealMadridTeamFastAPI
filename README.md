# RealMadridFastAPI

A FastAPI backend for managing Real Madrid player data, using MongoDB.

## Features

- CRUD operations for player data
- MongoDB integration
- CORS enabled for frontend access

## Requirements

- Python 3.9+
- MongoDB database (cloud or local)
- Docker (optional, for containerization)

## Local Development

1. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Set up MongoDB:**
    - Update the connection string in [`configuration.py`](configuration.py) if needed.

3. **Run the app:**
    ```sh
    uvicorn main:app --reload
    ```

## Docker

1. **Build the Docker image:**
    ```sh
    docker build -t realmadrid-fastapi -f .Dockerfile .
    ```

2. **Run the Docker container:**
    ```sh
    docker run -p 8000:8000 realmadrid-fastapi
    ```

## API Endpoints

- `GET /players/` - List all players
- `POST /players/` - Add a new player
- `PUT /players/{player_id}` - Update a player
- `DELETE /players/{player_id}` - Delete a player

## Project Structure

```
.
├── main.py
├── configuration.py
├── requirements.txt
├── .Dockerfile
├── database/
│   ├── models.py
│   └── schemas.py
└── ...
```

##