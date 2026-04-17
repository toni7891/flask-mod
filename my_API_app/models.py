import uuid
from flask import request
from werkzeug.exceptions import NotFound, BadRequest, UnprocessableEntity
from database import todos_collection
from bson.objectid import ObjectId

def getall():
    all_todos = list(todos_collection.find())
    for task in all_todos:
        task["_id"] = str(task["_id"])
        
    return all_todos 


def getby_id(id): 
    try:
        needed_task = todos_collection.find_one({"_id": ObjectId(id)})
        if needed_task:
            needed_task["_id"] = str(needed_task["_id"])
            return needed_task
    except:
        raise NotFound("ID provided does not exist in DB")

def post_new(data):   
    
    if not data or "title" not in data:
        raise UnprocessableEntity("the request body most be JSON")

    if not isinstance(data["title"], str):
        raise UnprocessableEntity("title must be a string")

    if not data["title"].strip():
        raise UnprocessableEntity("string cannot be empty or without spaces") 
    
    new_todo = {
        "title" : data.get("title"),
        "completed" : False
    }
    todos_collection.insert_one(new_todo)
    new_todo["_id"] = str(new_todo["_id"])
    return {
        "success" : True,
        "new task" : new_todo
    }
    
def edit_one(id):    
    update_data = request.json  
    
    if update_data == {}:
        raise BadRequest("the request body most be JSON")


    if not isinstance(update_data["title"], str):
        raise BadRequest("title must be a string")
    
    if not update_data["title"].strip():
        raise UnprocessableEntity("string cannot be empty or without spaces")
    if "completed" in update_data:
        if not isinstance(update_data["completed"], bool):
            raise BadRequest("state of completed must be BOOLean") 
    
    success = todos_collection.update_one(
        {"_id": ObjectId(id)},{
            "$set" : {
                "title": update_data["title"],
                "completed" : update_data["completed"]
            }})
    
    if success.matched_count == 0:
        raise NotFound("ID provided does not exist in DB")

    new_data ={
            "_id" : id,
            "title": update_data["title"],
            "completed" : update_data["completed"]
            }
    
    return new_data        
        
def delete_one(id):
    try:
        success = todos_collection.delete_one({"_id": ObjectId(id)})
        if success.deleted_count == 0:
                raise NotFound("ID provided does not exist in DB")
        return f"{id} has been deleted"
    except Exception:
        raise NotFound("ID provided does not exist in DB")
    