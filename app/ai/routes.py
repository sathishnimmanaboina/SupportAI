from flask import Blueprint, request, jsonify

from app.ai.service import analyze_ticket

ai_bp = Blueprint(
    "ai",
    __name__,
    url_prefix="/ai"
)


@ai_bp.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    result = analyze_ticket(
        data["title"],
        data["description"]
    )

    return jsonify(
        {
            "result": result
        }
    )