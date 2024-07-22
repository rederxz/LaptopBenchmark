from flask import Blueprint, request, jsonify
from app.services.user_service import register_user, login_user


user_bp = Blueprint("users", __name__)


@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user = register_user(data)
    return user, 201


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = login_user(data)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({"message": "Invalid credentials."}), 401
