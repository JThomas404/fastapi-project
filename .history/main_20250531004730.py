from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World"}

todos = []

# Get all todos

@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Get single todo

# Create a todo

@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "Todo has been added"}

# Update a todo

# Delete a todo