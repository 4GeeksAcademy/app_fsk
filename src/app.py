from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
model = load(open("./models/RandomForestClassifier_default_42.sav", "rb"))
class_dict = {
    "0": "Extrovertido",
    "1": "Introvertido",
    }

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
            val1 = int(request.form["val1"])
            val2 = int(request.form["val2"])
            val3 = int(request.form["val3"])
            val4 = int(request.form["val4"])
            val5 = int(request.form["val5"])
            val6 = int(request.form["val6"])
            val7 = int(request.form["val7"])

            data = ([[val1, val2, val3, val4, val5, val6, val7]])
            prediction = str(model.predict(data)[0])
            pred_class = class_dict[prediction]
    else:
        pred_class = None
    
    return render_template("index.html", prediction = pred_class)