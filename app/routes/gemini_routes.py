from flask import Blueprint, request, jsonify
import google.generativeai as genai

gemini_bp = Blueprint("gemini", __name__)

@gemini_bp.route("/gemini", methods=["POST"])
def ask_gemini():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "La question est requise"}), 400

    try:
        
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(question)
        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
