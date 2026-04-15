import uuid
from flask import request
from werkzeug.exceptions import NotFound, BadRequest, HTTPException, MethodNotAllowed, UnprocessableEntity


tasks = [
    {
        "id" : "1",
        "title" : "Learn Flask",
        "completed" : False
    },
    {
        "id" : "2",
        "title" : "Build API",
        "completed" : False
    },
    {
        "id" : "3",
        "title" : "Test with postman",
        "completed" : True
    },
]


def getall():
    return tasks


def getby_id(id):    
    for task in tasks:
        if  task["id"] == id:
            return task
    raise NotFound("ID provided does not exist in DB")

def post_new(data):   
    
    if not data or "title" not in data:
        raise BadRequest("the request body most be JSON")

    if not isinstance(data["title"], str):
        raise BadRequest("title must be a string")

    if not data["title"].strip():
        raise UnprocessableEntity("string cannot be empty or without spaces") 
    
    new_todo = {
        "id" : str(uuid.uuid4()),
        "title" : data["title"],
        "completed" : False
    }
    tasks.append(new_todo)
    
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
    
    if not isinstance(update_data["completed"], bool):
        raise BadRequest("state of completed must be BOOLean")       
    for task in tasks:
        if task["id"] == id:
            task["completed"] = update_data["completed"]
            task["title"] = update_data["title"] 
            return f"{task} updated"
        
    raise NotFound("ID provided does not exist in DB")
        
def delete_one(id):
    for ind, task in enumerate(tasks):
        if task["id"] == id:
            tasks.pop(ind)
            return f"{id} been deleted"
    raise NotFound("ID provided does not exist in DB")
    