import os
from flask import Flask, request, jsonify, send_from_directory
from google import genai

app = Flask(__name__, static_folder=".")

SYSTEM_PROMPT = 'You are a helpful study assistant. Explain academic topics simply, step by step. Encourage learning and avoid doing dishonest academic work.'
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

client = genai.Client(api_key=API_KEY) if API_KEY else None

@app.get("/")
def home():
    return send_from_directory(".", "index.html")

@app.post("/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"error": "Message is required."}), 400
    if not client:
        return jsonify({"error": "GEMINI_API_KEY is not configured in Render Environment Variables."}), 500
    try:
        prompt = SYSTEM_PROMPT + "\n\nUser message:\n" + message
        response = client.models.generate_content(model=MODEL, contents=prompt)
        return jsonify({"reply": response.text or "No response generated."})
    except Exception as e:
        return jsonify({"error": "AI request failed. Check the Render logs and API key."}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
