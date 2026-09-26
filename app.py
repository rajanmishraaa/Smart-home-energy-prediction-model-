from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("energy_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        household_size = int(request.form["household_size"])
        temperature = float(request.form["temperature"])
        has_ac = int(request.form["has_ac"])
        peak_usage = float(request.form["peak_usage"])
        day = int(request.form["day"])
        day_of_week = int(request.form["day_of_week"])
        is_weekend = int(request.form["is_weekend"])

        input_data = pd.DataFrame({
            "Household_Size": [household_size],
            "Avg_Temperature_C": [temperature],
            "Has_AC": [has_ac],
            "Peak_Hours_Usage_kWh": [peak_usage],
            "Day": [day],
            "Day_of_Week": [day_of_week],
            "Is_Weekend": [is_weekend]
        })

        prediction = model.predict(input_data)[0]

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)