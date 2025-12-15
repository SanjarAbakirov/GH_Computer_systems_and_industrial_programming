from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # ORM

app = Flask(__name__)

# Create Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"

db = SQLAlchemy(app)

# creating model


class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination
    country
    rating


# Create Routes


@app.route("/")
def home():
    return "Hello!"  # {}  # dictionary because we apply to JSON


if __name__ == "__main__":
    app.run(debug=True)
