from flask import Flask, render_template, request
import os
from joblib import load

app = Flask(__name__)

# Ruta al modelo
model_path = os.path.join("models", "./models/RandomForestClassifier_default_42.sav")
model = load(open(model_path, "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None
    if request.method == "POST":
        try:
            # Obtener los valores del formulario
            val1 = int(request.form["val1"])
            val2 = int(request.form["val2"])
            val3 = int(request.form["val3"])
            val4 = int(request.form["val4"])
            val5 = int(request.form["val5"])
            val6 = int(request.form["val6"])
            val7 = int(request.form["val7"])

            prediction = model.predict([[val1, val2, val3, val4, val5, val6, val7]])

        except Exception as e:
            error = str(e)

    return render_template("index.html", prediction=prediction, error=error)

if __name__ == "__main__":
    app.run(debug=True)
