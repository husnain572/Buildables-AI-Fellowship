from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    task: str

todos = []

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(todo: Todo):
    todos.append(todo.dict())
    return {"message": "Task added successfully!"}
