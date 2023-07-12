from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel): #receive from the client
    image_url: str
    title: str
    content: str
    creator: str

class PostDisplay(BaseModel):
    id: int
    image_url: str
    title: str
    content: str
    creator: str
    timestamp: datetime
    class Config():
        from_attributes = True