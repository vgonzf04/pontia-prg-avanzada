import requests
from fastapi import FastAPI, Response, status


from model.task import Task
from model.db import get_tasks_from_db, post_task_to_db, delete_task_on_db, put_completed_task_to_db, get_task_by_id_from_db, get_expired_tasks_from_db

from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

app = FastAPI()


@app.get("/tasks")
def get_tasks():
    return get_tasks_from_db()

@app.post("/tasks")
def create_task(task: Task, response: Response):
    post_task_to_db(task)
    response.status_code = status.HTTP_201_CREATED
    return task

@app.get("/tasks/expired")
def get_expired_tasks():
    return get_expired_tasks_from_db()

@app.get("/tasks/{id}")
def get_task_by_id(id: int):
    return get_task_by_id_from_db(id)

@app.put("/tasks/{id}")
def put_task(id:int):
    put_completed_task_to_db(id)

@app.delete("/tasks/{id}")
def delete_task(id: int):
    delete_task_on_db(id)