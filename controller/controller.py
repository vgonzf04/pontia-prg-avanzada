from fastapi import APIRouter, Response, status

from model.task import Task
from model.task_manager import task_manager

router = APIRouter()

@router.get("/tasks")
def get_tasks():
    return task_manager.get_tasks()

@router.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task, response: Response):
    return task_manager.post_task(task)

@router.get("/tasks/expired")
def get_expired_tasks():
    return task_manager.get_expired_tasks()

@router.get("/tasks/{id}")
def get_task_by_id(id: int):
    return task_manager.get_task_by_id(id)

@router.put("/tasks/{id}")
def put_task(id:int):
    return task_manager.put_completed_task(id)

@router.delete("/tasks/{id}")
def delete_task(id: int):
    return task_manager.delete_task(id)