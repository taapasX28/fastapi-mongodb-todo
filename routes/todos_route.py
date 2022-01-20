from time import sleep
from fastapi import APIRouter

from models.todos_model import Todo
from config.database import collection_name, producer, consumer

from schemas.todos_schema import todos_serializer, todo_serializer
from bson import ObjectId

todo_api_router = APIRouter()

# retrieve
@todo_api_router.get("/")
async def get_todos():
    todos = todos_serializer(collection_name.find())
    return todos

# post
@todo_api_router.post("/")
async def create_todo(todo: Todo):
    producer.send('todo1', dict(todo))
    for msg in consumer:
        message_val = msg.value
        break
    _id = collection_name.insert_one(message_val)
    return todos_serializer(collection_name.find({"_id": _id.inserted_id}))


# update
@todo_api_router.put("/{id}")
async def update_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(todo)
    })
    return todos_serializer(collection_name.find({"_id": ObjectId(id)}))

# delete
@todo_api_router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}