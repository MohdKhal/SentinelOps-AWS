from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "payment-service",
        "message": "Payment Service Running",
        "status": "success"
    })

@app.route("/payment")
def payment():
    return jsonify({
        "payment_id": "PAY001",
        "amount": 1800,
        "status": "SUCCESS"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
