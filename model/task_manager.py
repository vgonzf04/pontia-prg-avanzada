from datetime import date

from fastapi import HTTPException

from model.task import Task
import logging

logging.basicConfig(
    level=logging.INFO, # DEBUG INFO WARNING ERROR CRITICAL
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logs = logging.getLogger(__name__)

class TaskManager:

    def __init__(self):
        self.__tasks = []
        self.__next_id = 1

    def get_tasks(self):
        tasks = self.__tasks
        if tasks == []:
            logs.error("No task has been found")
            raise HTTPException(status_code=404, detail="No task has been found")
        logs.info("Tasks have been found")
        return tasks


    def post_task(self, task: Task):
        existing = self.__get_task_by_title(task.title)
        if existing:
            logs.error("Task already created")
            raise HTTPException(status_code=400, detail="Task already created")

        new_task = {
            "id": self.__next_id,
            "title": task.title,  
            "description": task.description, 
            "deadline": task.deadline, 
            "completed": task.completed

        }
        
        self.__tasks.append(new_task)
        self.__next_id += 1
        logs.info(f"Task with id:{new_task["id"]} created")

        return new_task

    def get_task_by_id(self, id: int):
        
        task = self.__get_task_by_id(id)
        if task is None:
            logs.error(f"Task with id:{id} doesn't exist")
            raise HTTPException(status_code=404, detail=f"Task with id:{id} doesn't exist")
        
        logs.info(f"Task with id:{id} found")
        return task

    def get_expired_tasks(self):
        expired_tasks = []

        for task in self.__tasks:
            if task["deadline"] < date.today():
                expired_tasks.append(task)

        if expired_tasks == []:
            logs.info("No expired tasks were found")
            raise HTTPException(status_code=404, detail="No expired tasks were found")
        
        logs.info("Expired tasks were found")
        return expired_tasks


    def put_completed_task(self, id: int):
        task_to_update = self.__get_task_by_id(id)

        if task_to_update is None:
            logs.error(f"Task with id:{id} doesn't exist")
            raise HTTPException(status_code=404, detail=f"Task with id:{id} doesn't exist")

        if task_to_update["completed"]:
            logs.error(f"Task with id:{id} already finished")
            raise HTTPException(status_code=400, detail=f"Task with id:{id} already finished")

        task_to_update["completed"] = True
        logs.info(f"Task with id:{id} marked as finished")
        return {f"msg": "Task with id:{id} marked as finished"}

    def delete_task(self, id: int):
        task_to_delete = self.__get_task_by_id(id)
        if task_to_delete is None:
            logs.error(f"Task with id:{id} not found")
            raise HTTPException(status_code=404, detail=f"Task with id:{id} not found")
        self.__tasks.remove(task_to_delete)
        logs.info(f"Task with id:{id} deleted")

        return {"msg": f"Task with id:{id} deleted"}

    def __get_task_by_id(self, id: int):
        for task in self.__tasks:
            if task["id"] == id:
                return task
        return None

    def __get_task_by_title(self, title: str):
        for task in self.__tasks:
            if task["title"] == title:
                return task
        return None

task_manager = TaskManager()