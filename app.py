from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Flask CI/CD Demo",
        "environment": os.getenv("APP_ENV"),
        "api_key": os.getenv("DEMO_API_KEY")
    }

if __name__ == "__main__":
    app.run(debug=True)