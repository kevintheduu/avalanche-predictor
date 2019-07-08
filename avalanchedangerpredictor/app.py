import random
import pandas as pd
from sklearn.pipeline import Pipeline
import pickle
from flask import Flask, request, render_template, jsonify


with open('spam_model.pkl', 'rb') as f:
    model = pickle.load(f)
app = Flask(__name__, static_url_path="")

@app.route('/')
def index():
    """Return the main page."""
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Return a random prediction."""
    """First lets see if it can return what I want"""
    data = request.json
    #prediction = model.predict_proba([data['user_input']])
    #return jsonify({'probability': prediction[0][1]})
    return request.json