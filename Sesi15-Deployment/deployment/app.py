import pickle
import pandas as pd
from flask import Flask, request

app = Flask(__name__)

with open("pipeline.pkl","rb") as f:
    model = pickle.load(f)

def predict_data(new_data, model):
    columns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
    df_data = pd.DataFrame([new_data], columns=columns)
    res = model.predict(df_data)
    return "Survived" if res[0] == 1 else "Not Survived"

@app.route("/")
def halo():
    args = request.args
    pclass = args.get("pclass", type=float, default=0)
    sex = args.get("sex", type=float, default=0)
    age = args.get("age", type=float, default=0)
    sibsp = args.get("sibsp", type=float, default=0)
    parch = args.get("parch", type=float, default=0)
    fare = args.get("fare", type=float, default=0)
    new_data = [pclass, sex, age, sibsp, parch, fare]
    res = predict_data(new_data, model)
    return {'result':res}

app.run(debug=True)