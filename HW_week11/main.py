from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Create Database


# Create Routes

@app.route("/")
def home():
    return "Hello!"  # {}  # dictionary because we apply to JSON


if __name__ == "__main__":
    app.run(debug=True)
