from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from configuration import collection
from database.schemas import all_players
from database.models import Team
from bson.objectid import ObjectId

app = FastAPI()
router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://real-madrid-team-fast-api.vercel.app/"],  # ✅ your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@router.get("/")
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
async def update_player(player_id:str, updated_player:Team):
     collection.find_one_and_update({"_id": ObjectId(player_id)}, {"$set":dict(updated_player)})

@router.delete("/{player_id}")
async def delete_player(player_id: str):
    collection.find_one_and_delete({"_id":ObjectId(player_id)})


app.include_router(router)

# @app.get('/')
# async def homepage():
#     return {"message": "Hello world!!!"}