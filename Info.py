import os

class Info:
    API_ID = os.getenv("API_ID", "20919625")
    API_HASH = os.getenv("API_HASH", "40168846bf06f4ff443f0f7a4182bf8d")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    OWNER_ID = int(os.getenv("OWNER_ID", "6233910543"))

    MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://hicit73592:Sf3ketW4B0pFTgvd@cluster0.aa2c7wh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "captionbot")
