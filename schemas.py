# Schema class for movie
from typing import Optional
from pydantic import BaseModel

class MovieBase(BaseModel):
    name: str
    lang: str

class Movie(MovieBase):
    id: int
    class Config:
        orm_mode = True