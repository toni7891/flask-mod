from flask import Flask, render_template
from routes import tasks_bp
from errors import errors_bp
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi
from database import init_db

app = Flask(__name__)
init_db(app)
load_dotenv()
mongo_connection_string = os.getenv("MONGO_URI")
cr = certifi.where()
client = MongoClient(mongo_connection_string, tlsCAFile=cr, serverSelectionTimeoutMS=2000)
db = client['app_todo']
todos_collection = db['data']


app.register_blueprint(tasks_bp)
app.register_blueprint(errors_bp)

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)