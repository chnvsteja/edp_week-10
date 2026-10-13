
from flask import Flask, render_template, request
from src.predict import predict_fraud

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            transaction = {
                "transaction_id": request.form["transaction_id"],
                "amount": request.form["amount"],
                "transaction_hour": request.form["transaction_hour"],
                "merchant_category": request.form["merchant_category"],
                "foreign_transaction": int(
                    request.form["foreign_transaction"]
                ),
                "location_mismatch": int(
                    request.form["location_mismatch"]
                ),
                "device_trust_score": request.form["device_trust_score"],
                "velocity_last_24h": request.form["velocity_last_24h"],
                "cardholder_age": request.form["cardholder_age"],
            }

            result = predict_fraud(transaction)

        except Exception as exc:
            app.logger.exception("Prediction failed")
            error = str(exc)

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
