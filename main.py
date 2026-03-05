from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db.database import get_db
# from db.models import Test
from api.v1.router import route
from routes.curd_routes import curd_routes

app = FastAPI()

app.include_router(route)
app.include_router(curd_routes)

@app.get("/")
def home(db: Session = Depends(get_db)):
    return {
        "name": "Ritik"
    }

# @app.get("/users")
# def get_users(db: Session = Depends(get_db)):
#     users = db.query(Test).all()
#     return users

