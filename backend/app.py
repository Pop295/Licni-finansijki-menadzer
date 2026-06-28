from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # dozvoljava Vue da pristupi backendu

@app.route("/")
def home():
    return jsonify({"message": "Backend radi!"})

@app.route("/api/transactions")
def transactions():
    data = [
        {"id": 1, "title": "Plata", "amount": 1000},
        {"id": 2, "title": "Hrana", "amount": -50}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)