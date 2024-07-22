from flask import Blueprint, request, jsonify
from app.services.notebook_service import add_notebook


notebook_bp = Blueprint("notebooks", __name__)


@notebook_bp.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    notebook = add_notebook(data)
    jsonify(notebook), 201
