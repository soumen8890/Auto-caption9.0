from pymongo import MongoClient
from Info import Info

client = MongoClient(Info.MONGO_URI)
db = client[Info.DATABASE_NAME]

captions = db["captions"]
