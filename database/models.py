from pydantic import BaseModel

class Team(BaseModel):
    type: str
    position: str
    number: str
    firstname: str
    surname: str
    placebirth: str
    datebirth: str
    weight: str
    height: str
    img:str