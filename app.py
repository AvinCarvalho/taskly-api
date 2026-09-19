from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],

)
@app.get("/")
def home():
    return {"message": "Taskly API is running!"}


client = MongoClient("mongodb://mongodb:27017")

db = client.taskly
todos = db.todos


@app.get("/todos")
def get_todos():
    all_todos = list(todos.find({}, {"_id": 0}))
    return all_todos


@app.post("/todos")
def add_todo(todo: dict):
    todos.insert_one(todo)
    return {"message": "Todo added!"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    todos.delete_one({"_id": ObjectId(todo_id)})
    return {"message": "Todo deleted!"}
