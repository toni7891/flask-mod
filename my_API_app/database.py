from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()
mongo_connection_string = os.getenv("MONGO_URI")
cr = certifi.where()
client = MongoClient(mongo_connection_string, tlsCAFile=cr, serverSelectionTimeoutMS=2000)
db = client['app_todo']
todos_collection = db['data']