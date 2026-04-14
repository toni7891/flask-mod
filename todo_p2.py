from flask import Flask, jsonify, request 
import uuid
app = Flask(__name__)

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

@app.route('/tasks', methods=['GET', 'POST'])
def taskss():
    if request.method == "POST":
        title = request.json
        if not bool(title):
            return f"ERROR" , 400
        
        new_todo = {
            "id" : str(uuid.uuid4()),
            "title" : title["title"],
            "completed" : False
        }
        tasks.append(new_todo)
        return jsonify({
            "success" : True,
            "new task" : new_todo
        }), 200
        
        
    if request.method == "GET":
        return jsonify(tasks)

@app.route('/tasks/<id>', methods=["GET", "PUT", "DELETE"])
def getbyid(id):
    
    if request.method == "GET":
        success = False
        for task in tasks:
            if  task["id"] == id:
                success = True
                return jsonify({
                    "success" : success,
                    "task" : task 
                })
        if success == False:
            return jsonify({
                "error" : "id not found",
                "id to search" : id
            })
            
    if request.method == "PUT":
        data = request.json
        for task in tasks:
            if task["id"] == id:
                if "completed" in data:
                    task["completed"] = data["completed"]
                if "title" in data:
                    task["title"] = data["title"] 
                return f"{task} updated"
        
        return f"ERROR", 400
        
    if request.method == "DELETE":
        for ind, task in enumerate(tasks):
            if task["id"] == id:
                tasks.pop(ind)
                return f"{id} been deleted"
        
        


if __name__ == "__main__":
    app.run(debug=True)