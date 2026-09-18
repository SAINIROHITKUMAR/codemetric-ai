from flask import Blueprint, jsonify, request
from app.analyzer.metrics import analyze_code

api = Blueprint("api", __name__)

@api.get("/health")
def health():
    return jsonify({"status": "success", "message": "CodeMetric AI API is running"})

@api.post("/analyze")
def analyze():
    data = request.get_json(silent=True) or {}
    code = data.get("code")

    if not isinstance(code, str) or not code.strip():
        return jsonify({"status": "error", "message": "Non-empty Python code is required"}), 400

    try:
        result = analyze_code(code)
        return jsonify({"status": "success", "data": result})
    except SyntaxError as exc:
        return jsonify({
            "status": "error",
            "message": "Invalid Python syntax",
            "details": str(exc)
        }), 400
    except Exception as exc:
        return jsonify({"status": "error", "message": str(exc)}), 500
