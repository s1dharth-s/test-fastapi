from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

from typing import List
from imdb_details import get_details_imdb

import models, schemas
from database import SessionLocal, engine

#initialise db
models.Base.metadata.create_all(bind=engine)

#initialise app
app = FastAPI()

# Dependency for database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def home():
    return {'hello': 'world'}

@app.post('/movie', response_model= schemas.Movie)
def post_movie(movie: schemas.MovieBase, db: Session = Depends(get_db)):
    new_movie = models.Movie(name=movie.name, lang=movie.lang)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie
   
@app.get('/movie', response_model=List[schemas.Movie])
def get_movies(db: Session = Depends(get_db)):
    return db.query(models.Movie).all()

@app.get('/movie/{id}', response_model= schemas.Movie)
def movie_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(models.Movie).filter(models.Movie.id == id).first()

@app.get('/movie/details/{id}')
def get_details(id: int, db: Session = Depends(get_db)):
    mov = db.query(models.Movie).filter(models.Movie.id == id).first()
    return get_details_imdb(mov.name)
