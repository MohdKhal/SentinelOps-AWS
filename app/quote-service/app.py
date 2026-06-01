from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "quote-service",
        "message": "Quote Service Running",
        "status": "success"
    })

@app.route("/quote")
def quote():
    return jsonify({
        "destination": "Dubai",
        "days": 7,
        "quote": 1800
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
