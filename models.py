from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    lang = Column(String)
