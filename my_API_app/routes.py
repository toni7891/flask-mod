from flask import jsonify, request, Blueprint
from werkzeug.exceptions import MethodNotAllowed
from models import getall, getby_id, post_new, edit_one, delete_one

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route('/tasks', methods=["GET", "POST"])
def taskss():
    if request.method not in ["GET","POST"]:
        raise MethodNotAllowed("incorrect method for request")
    
    if request.method == "POST":
        data_new = request.json
        return jsonify(post_new(data_new)),201
    
    if request.method == "GET":
        return jsonify(getall())
    

@tasks_bp.route('/tasks/<id>', methods=["GET", "PUT", "DELETE"])
def getbyid(id):    
    if request.method not in ["GET", "PUT", "DELETE"]:
        raise MethodNotAllowed("incorrect method for request")
    
    if request.method == "GET":        
        return jsonify(getby_id(id)),200
            
    if request.method == "PUT":
        return jsonify(edit_one(id)),200
        
    if request.method == "DELETE":
        return jsonify(delete_one(id)),200
