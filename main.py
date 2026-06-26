from fastapi import FastAPI

import controller.controller as controller
from model.task_manager import logs

app = FastAPI()
app.include_router(controller.router)

@app.get("/")
def root():
    logs.info("API working correctly.")
    return {"msg": "API working correctly."}