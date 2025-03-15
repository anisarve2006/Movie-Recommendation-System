from flask import Flask, request, jsonify
from flask_cors import CORS
from model import recommend_movies

app = Flask(__name__)
CORS(app)  # Allows frontend to access backend

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    interests = data.get("interests", "")
    recommended_movies = recommend_movies(interests)
    return jsonify({"movies": recommended_movies})

if __name__ == '__main__':
    app.run(debug=True)
