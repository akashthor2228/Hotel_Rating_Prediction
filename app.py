from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# 🔥 Load model, scaler, imputer
model = pickle.load(open("dtr_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
imputer = pickle.load(open("imputer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # 1️⃣ raw input
    input_data = np.array([[
        data["avg_cost"],
        data["table_booking"],
        data["online_delivery"],
        data["delivering_now"],
        data["price_range"],
        data["votes"]
    ]])

    # 2️⃣ impute missing values
    input_data = imputer.transform(input_data)

    # 3️⃣ scale data
    input_data = scaler.transform(input_data)

    # 4️⃣ prediction
    prediction = model.predict(input_data)[0]
    prediction = round(float(prediction), 2)

    return jsonify({"rating": prediction})

if __name__ == "__main__":
    app.run(debug=True)
