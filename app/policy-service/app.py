from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "policy-service",
        "message": "Policy Service Running",
        "status": "success"
    })

@app.route("/policies")
def policies():
    return jsonify([
        {
            "policy_id": 101,
            "type": "Travel Insurance",
            "premium": 1200
        }
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
