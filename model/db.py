from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Date

from datetime import date

from fastapi import HTTPException

from model.task import Task
import logging

logging.basicConfig(
    level=logging.INFO, # DEBUG INFO WARNING ERROR CRITICAL
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logs = logging.getLogger(__name__)

DATABASE_URL = "sqlite:///./tasks.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    deadline = Column(Date, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)


def get_tasks_from_db():
    db = SessionLocal()
    tasks = db.query(TaskDB).all()
    db.close()
    if tasks == []:
        logs.error("No task has been found")
        raise HTTPException(status_code=404, detail="No task has been found")
    logs.info("Tasks have been found")
    return tasks


def post_task_to_db(task: Task):
    db = SessionLocal()
    existing = db.query(TaskDB).filter(TaskDB.title == task.title).first()
    if existing:
        db.close()
        logs.error("Task already created")
        raise HTTPException(status_code=400, detail="Task already created")

    task_db = TaskDB(title=task.title, description=task.description, deadline=task.deadline, completed=task.completed)
    db.add(task_db)
    db.commit()
    db.refresh(task_db)
    db.close()
    logs.info(f"Task with id:{task_db.id} created")

def get_task_by_id_from_db(id: int):
    db = SessionLocal()
    task = __get_task_by_id(id, db)
    db.close()
    if not task:
        logs.error("Task with id:{id} doesn't exist")
        raise HTTPException(status_code=404, detail=f"Task with id:{id} doesn't exist")
    
    logs.info(f"Task with id:{id} found")
    return task

def get_expired_tasks_from_db():
    db = SessionLocal()
    expired_tasks = db.query(TaskDB).filter(TaskDB.deadline < date.today()).all()
    db.close()
    if expired_tasks == []:
        logs.info("No expired tasks were found")
        raise HTTPException(status_code=404, detail="No expired tasks were found")
    
    logs.info("Expired tasks were found")
    return expired_tasks


def put_completed_task_to_db(id: int):
    db = SessionLocal()
    task_to_update = __get_task_by_id(id, db)
    if task_to_update.completed:
        db.close()
        logs.error(f"Task with id:{id} already finished")
        raise HTTPException(status_code=400, detail=f"Task with id:{id} already finished")

    task_to_update.completed = True
    db.commit()
    db.close()
    logs.info(f"Task with id:{id} marked as finished")

def delete_task_on_db(id: int):
    db = SessionLocal()
    task_to_delete = __get_task_by_id(id, db)
    if not task_to_delete:
        db.close()
        logs.error(f"Task with id:{id} not found")
        raise HTTPException(status_code=404, detail=f"Task with id:{id} not found")
    db.delete(task_to_delete)
    db.commit()
    db.close()
    logs.info(f"Task with id:{id} deleted")

def __get_task_by_id(id: int, db):
    return db.query(TaskDB).get(id)