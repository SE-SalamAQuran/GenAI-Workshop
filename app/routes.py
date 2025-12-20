from flask import Blueprint, request, jsonify
from app.prompts import build_prompt
from app.llm import mock_llm
from app.schemas import validate_request

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    error = validate_request(data)
    if error:
        return jsonify({"error": error}), 400

    prompt = build_prompt(data["text"])
    result = mock_llm(prompt)

    return jsonify({
        "prompt_used": prompt,
        "result": result
    })
