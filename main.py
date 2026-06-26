from fastapi import FastAPI

from model.db import Base, engine
from controller.controller import router

from model.db import logs 

Base.metadata.create_all(bind=engine)
logs.info("Database table created")

app = FastAPI()
app.include_router(router)

@app.get("/")
def root():
    logs.info("API working correctly.")
    return {"msg": "API working correctly."}