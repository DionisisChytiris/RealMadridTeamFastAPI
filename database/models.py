from pydantic import BaseModel
from typing import Optional

class Team(BaseModel):
    type: Optional[str] = None
    position: str
    number: str
    firstname: str
    surname: str
    placebirth: Optional[str] = None
    datebirth: Optional[str] = None
    weight: Optional[str] = None
    height: Optional[str] = None
    img: Optional[str] = ""