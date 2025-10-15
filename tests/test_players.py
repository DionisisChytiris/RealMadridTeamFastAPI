# tests/test_players.py
from bson import ObjectId

def seed_player(coll, **overrides):
    base = {
        "type": None, "position": "MF", "number": "8",
        "firstname": "Toni", "surname": "Kroos",
        "placebirth": "", "datebirth": "", "weight": "", "height": "", "img": ""
    }
    base.update(overrides)
    return coll.insert_one(base).inserted_id

def test_root(client):
    r = client.get("/")
    assert r.status_code == 200
    assert "FastAPI backend is running" in r.json()["message"]

def test_get_players(client, mock_collection):
    _id = seed_player(mock_collection, firstname="Luka", surname="Modrić", number="10")
    r = client.get("/players/")
    assert r.status_code == 200
    data = r.json()
    assert any(p["id"] == str(_id) and p["firstname"] == "Luka" for p in data)

def test_create_player(client, mock_collection):
    payload = {
        "position": "FW", "number": "7", "firstname": "Vinícius", "surname": "Júnior",
        "type": None, "placebirth": "", "datebirth": "", "weight": "", "height": "", "img": ""
    }
    r = client.post("/players/", json=payload)
    assert r.status_code == 200
    assert "id" in r.json()

def test_update_player(client, mock_collection):
    _id = seed_player(mock_collection, firstname="Jude", surname="Bellingham", number="5")
    updated = {
        "position": "MF", "number": "5", "firstname": "Jude", "surname": "Bellingham",
        "type": None, "placebirth": "", "datebirth": "", "weight": "", "height": "", "img": ""
    }
    r = client.put(f"/players/{_id}", json=updated)
    assert r.status_code == 200
    assert r.json()["message"] == "Player updated successfully"

def test_delete_player(client, mock_collection):
    _id = seed_player(mock_collection, firstname="Thibaut", surname="Courtois", number="1")
    r = client.delete(f"/players/{_id}")
    assert r.status_code == 200
    assert r.json()["message"] == "Player deleted successfully"