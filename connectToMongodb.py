from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_PWD = os.getenv('MONGODB_PWD')

if not MONGODB_PWD:
    raise ValueError("MongoDB password is not set in the environment variables.")

uri = f"mongodb+srv://root:{MONGODB_PWD}@one.7glm8.mongodb.net/?retryWrites=true&w=majority&appName=one"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
