from flask import Flask, request, jsonify
from model import recommend_jobs
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows the frontend (React) to talk to Flask

@app.route("/")
def home():
    return "Career Recommender API is running!"

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    user_skills = data.get("skills", "")
    
    if not user_skills:
        return jsonify({"error": "No skills provided"}), 400
    
    recommendations = recommend_jobs(user_skills)
    return jsonify(recommendations)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
