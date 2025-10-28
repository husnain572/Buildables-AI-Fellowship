from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI()

API_KEY = "secret"

class Todo(BaseModel):
    task: str

todos = []

@app.get("/todos")
def get_todos(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return todos

@app.post("/todos")
def add_todo(todo: Todo, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    todos.append(todo.dict())
    return {"message": "Task added successfully!"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    if todo_id >= len(todos) or todo_id < 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos.pop(todo_id)
    return {"message": "Task deleted successfully!"}
