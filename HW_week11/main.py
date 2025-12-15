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
# http://www.thenerdnook.io/destinations


@app.route("/destinations", methods=["GET"])
def get_destinations():
    # fetch every raw in db with json format
    destinations = Destination.query.all()

    return jsonify([destination.to_dict()] for destination in destinations)

# http://www.thenerdnook.io/destinations/2


@app.route("/destinations/<int:destination_id>", methods=["GET"])
def get_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination:
        return jsonify(destination_id.to_dict())
    else:
        return jsonify({"error": "Destination not found!"}), 404

# app (to send inf to api)
# POST Request


@app.route("/destinations", methods=["POST"])
def add_destination():
    # parse incoming json body to abstract data
    data = request.get_json()
    # insert it ot new db
    new_destination = Destination(destination=data["destination"],
                                  country=data["country"],
                                  rating=data['rating'])
    # as a record
    db.session.add(new_destination)
    db.session.commit()

    return jsonify(new_destination.to_dict()), 201

# PUT -> UPDATE


@app.route("/destination/<int:destination_id>", methods=["PUT"])
def update_destination(destination_id):
    data = request.get_json()
    destination = Destination.query.get(destination_id)
    if destination:
        destination.destination = data.get(
            "destination", destination.destination)
        destination.country = data.get(
            "country", destination.destination)
        destination.rating = data.get(
            "rating", destination.destination)

        db.session.commit()
        return jsonify(destination.to_dict())
    else:
        return jsonify({"error": "Destination not found!"}), 404

# Delete


if __name__ == "__main__":
    app.run(debug=True)
