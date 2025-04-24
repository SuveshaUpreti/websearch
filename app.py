from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)
SERPAPI_KEY = "cd36c1c9a55a954cf5a8cff90725b795e1d0b41c3f73c7711c03e650ac6121bf"

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/search")
def search():
    query = request.args.get("q")
    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY
    }
    response = requests.get(url, params=params)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
