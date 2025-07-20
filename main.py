from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from configuration import collection
from database.schemas import all_players
from database.models import Team
from bson.objectid import ObjectId
from pymongo import ReturnDocument

app = FastAPI()
router = APIRouter()

origins = [
    "https://real-madrid-app.vercel.app",  # ✅ Production frontend
    "http://localhost:5173",               # ✅ Local development frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ✅ your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@router.get("/", tags=["Players"])
async def get_all_players():
    data = collection.find()
    return all_players(data)

@router.post("/")
async def create_player(new_player:Team):
    try:
        res = collection.insert_one(dict(new_player))
        return {"status_code": 200, "id": str(res.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured{e}")

@router.put("/{player_id}")
async def update_player(player_id: str, updated_player: Team):
    result = collection.find_one_and_update(
        {"_id": ObjectId(player_id)},
        {"$set": dict(updated_player)},
        return_document=ReturnDocument.AFTER,  # <-- fix here
    )
    if result:
        return {"message": "Player updated successfully"}
    raise HTTPException(status_code=404, detail="Player not found")


@router.delete("/{player_id}")
async def delete_player(player_id: str):
    result = collection.find_one_and_delete({"_id": ObjectId(player_id)})
    if result:
        return {"message": "Player deleted successfully"}
    raise HTTPException(status_code=404, detail="Player not found")
    
# @router.put("/{player_id}")
# async def update_player(player_id:str, updated_player:Team):
#      collection.find_one_and_update({"_id": ObjectId(player_id)}, {"$set":dict(updated_player)})

# @router.delete("/{player_id}")
# async def delete_player(player_id: str):
#     collection.find_one_and_delete({"_id":ObjectId(player_id)})


app.include_router(router, prefix="/players")

# @app.get('/')
# async def homepage():
#     return {"message": "Hello world!!!"}