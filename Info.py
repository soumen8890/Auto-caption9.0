import os

class Info:
    API_ID = os.getenv("API_ID", "your_api_id")
    API_HASH = os.getenv("API_HASH", "your_api_hash")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
    OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))

    MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://user:pass@cluster/db")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "captionbot")
