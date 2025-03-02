from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the new trained model
model = joblib.load("model/house_price_rf_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Fetch user input
            user_input = [
                float(request.form["LotArea"]),
                float(request.form["OverallQual"]),
                float(request.form["OverallCond"]),
                float(request.form["YearBuilt"]),
                float(request.form["TotalBsmtSF"]),
                float(request.form["GrLivArea"]),
                float(request.form["FullBath"]),
                float(request.form["HalfBath"]),
                float(request.form["GarageCars"]),
                float(request.form["GarageArea"]),
            ]
            # Convert to numpy array
            features_array = np.array([user_input])

            # Make prediction
            predicted_price = model.predict(features_array)[0]
            predicted_price = round(predicted_price, 2)

            return render_template("result.html", price=predicted_price)
        
        except Exception as e:
            return render_template("result.html", error=str(e))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
