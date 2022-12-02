from flask import Flask, jsonify, request
from flask_cors import CORS

from .entities.entity import Base, Session, engine
from .entities.match import Match, MatchSchema

app = Flask(__name__)
CORS(app)

Base.metadata.create_all(engine)


@app.route("/matches")
def get_matches():
    session = Session()
    matches_objects = session.query(Match).all()

    schema = MatchSchema(many=True)
    matches = schema.dump(matches_objects)

    session.close()

    return jsonify(matches)


@app.route("/matches", methods=["POST"])
def add_match():
    posted_match = MatchSchema(
        only=(
            "match_id",
            "player_0",
            "player_1",
            "player_2",
            "player_3",
            "player_4",
            "player_5",
            "player_6",
            "player_7",
            "player_8",
            "player_9",
        )
    ).load(request.get_json())

    match = Match(**posted_match, created_by="HTTP post request")

    session = Session()
    session.add(match)
    session.commit()

    new_match = MatchSchema().dump(match)
    session.close()

    return jsonify(new_match), 201
