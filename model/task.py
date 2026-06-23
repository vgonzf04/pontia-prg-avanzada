# tabla de task
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class Task(BaseModel):
    title: str = Field(..., max_length=30, description="Task title (max 30)")
    description: Optional[str] = Field(None, max_length=50, decription="Task description, (max 50)")
    deadline: date = Field(..., description="Task due date (YYYY-MM-DD)")
    completed: bool = Field(default=False, description="Is it done? (True/False)")