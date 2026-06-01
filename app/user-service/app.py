from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "user-service",
        "message": "User Service Running",
        "status": "success"
    })

@app.route("/users")
def users():
    return jsonify([
        {
            "id": 1,
            "name": "Mohd Ibrahim"
        }
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
