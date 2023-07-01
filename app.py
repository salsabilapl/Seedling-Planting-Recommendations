
#import imp
#from pyexpat import features



import pandas as pd
from flask import Flask, request, render_template
import pickle
import joblib
from sklearn.tree import DecisionTreeClassifier
import numpy as np

app = Flask(__name__)
model_file = open('agriculture_model.pkl', 'rb')
model = joblib.load(model_file)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    
    N = request.form['N']
    P = request.form['P']
    K = request.form['K']
    temperature = request.form['temperature']
    humidity = request.form['humidity']
    ph = request.form['ph']
    rainfall = request.form['rainfall']
    
    data_pred = np.array([N,P,K,temperature,humidity,ph,rainfall]).reshape(1, -1)
    
    model_prediction = model.predict(data_pred)[0]

    return render_template("index.html", prediction_text=model_prediction)

if __name__ == "__main__":
    app.run(debug=True)
