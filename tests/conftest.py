# tests/conftest.py
import mongomock
import pytest
from fastapi.testclient import TestClient
import main

@pytest.fixture()
def mock_collection(monkeypatch):
    client = mongomock.MongoClient()
    db = client["team_db"]
    coll = db["team_data"]
    monkeypatch.setattr(main, "collection", coll)  # override the imported symbol in main.py
    return coll

@pytest.fixture()
def client():
    return TestClient(main.app)