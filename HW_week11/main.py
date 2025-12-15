from flask import Flask, jsonify, request  # get post put and delete
from flask_sqlalchemy import SQLAlchemy  # ORM

app = Flask(__name__)

# Create Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"

db = SQLAlchemy(app)

# build out the model


class Destination(db.Model):
    # to let api fetch the inf like raw and columns
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "destination": self.destination,
            "country": self.country,
            "rating": self.rating
        }


# last thing we need to set up the db:
with app.app_context():
    db.create_all()

# http://www.thenerdnook.io/
# Create Routes


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Travel API"})


if __name__ == "__main__":
    app.run(debug=True)
