from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Telegram Auto Caption Bot is running!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render uses PORT env
    app.run(host="0.0.0.0", port=port)
