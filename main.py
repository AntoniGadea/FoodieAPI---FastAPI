from fastapi import FastAPI
from core.config import settings
from db.session import engine 
from db.base_class import Base

from app.routers import users


def create_tables():         
	Base.metadata.create_all(bind=engine)
        

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()

app.include_router(users.router)

@app.get("/")
def home():
    return {"msg":"Hello FastAPI🚀"}

