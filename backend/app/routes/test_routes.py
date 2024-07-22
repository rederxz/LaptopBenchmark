from flask import Blueprint, request, jsonify
from app.models import db
from app.services.test_service import TestService


test_bp = Blueprint("tests", __name__)


@test_bp.route("/add", methods=["POST"])
def add():
    data = request.get_json()

    user_id = data.get("user_id")
    notebook_id = data.get("notebook_id")
    testtag_id = data.get("testtag_id")
    score = data.get("score")

    if not all([user_id, notebook_id, testtag_id, score]):
        return jsonify({"message": "Missing data."}), 400

    service = TestService(db.session)
    test = service.add_test(user_id, notebook_id, testtag_id, score)

    return jsonify(test), 201
