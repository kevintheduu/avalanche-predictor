import random
import pandas as pd
from sklearn.pipeline import Pipeline
import pickle
from flask import Flask, request, render_template, jsonify
import numpy as np

def apply_scaling_factor(num):
    """Applies a scaling factor to the model's prediction.
    Will need to be recalibrated every month of the season to
    adjust for new data."""
    scaling_factor = 1.5
    y_pred_5_percentile = 1.2
    y_scaled = ((num-y_pred_5_percentile) * scaling_factor) +1
    return y_scaled

with open('avy_danger_prediction2.pkl', 'rb') as f:
    model = pickle.load(f)
app = Flask(__name__, static_url_path="")

@app.route('/')
def index():
    """Return the main page."""
    return render_template('index.html')

# Index([, 'Temperature (deg F)',
    #    'Wind Speed Minimum (mph)', 'Wind Speed Average (mph)',
    #    'Wind Speed Maximum (mph)', 'Wind Direction (deg.)',
    #    'Total Snow Depth (in)', 'max_1_day_temp', 'min_1_day_temp',
    #    'max_2_day_temp', 'min_2_day_temp', 'max_1_day_snow', 'max_2_day_snow',
    #    'max_3_day_snow', '4800_brooks'],
    #   dtype='object')
    

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Return a predicted avalanche danger level through the regression model."""
    
    data = request.json
    #prediction = model.predict_proba([data['user_input']])
    #return jsonify({'probability': prediction[0][1]})
    print(data)
    # input_solar_text = data['input_solar_01']
    # print(input_solar_text, type(input_solar_text))
    # input_solar = float(input_solar_text)
    
    input_temp_text = data['input_temp_02']
    input_temp = float(input_temp_text)
    
    input_wind_speed_min_text = data['input_wind_speed_min_03']
    input_wind_speed_min = float(input_wind_speed_min_text)

    input_wind_speed_avg_text = data['input_wind_speed_avg_04']
    input_wind_speed_avg = float(input_wind_speed_avg_text)

    input_wind_speed_max_text = data['input_wind_speed_max_05']
    input_wind_speed_max = float(input_wind_speed_max_text)
    
    input_wind_direction_text = data['input_wind_direction_06']
    input_wind_direction = float(input_wind_direction_text)
    
    input_snowpack_height_text = data['input_snowpack_height_07']
    input_snowpack_height = float(input_snowpack_height_text)
    
    input_1day_max_temp_text = data['input_1day_max_temp_08']
    input_1day_max_temp = float(input_1day_max_temp_text)

    input_1day_min_temp_text = data['input_1day_min_temp_09']
    input_1day_min_temp = float(input_1day_min_temp_text)
    
    input_2day_max_temp_text = data['input_2day_max_temp_10']
    input_2day_max_temp = float(input_2day_max_temp_text)
    
    input_2_day_min_temp_text = data['input_2_day_min_temp_11']
    input_2_day_min_temp = float(input_2_day_min_temp_text)
    
    input_1day_max_snow_text = data['input_1day_max_snow_12']
    input_max_1_day_snow = float(input_1day_max_snow_text)
    
    input_2day_max_snow_text = data['input_2day_max_snow_13']
    input_2day_max_snow = float(input_2day_max_snow_text)
    
    input_3day_max_snow_text = data['input_3day_max_snow_14']
    input_3day_max_snow = float(input_3day_max_snow_text)
    
    input_precip_text = data['input_precip_15']
    input_precip = float(input_precip_text)
    
    arguments = pd.DataFrame([[
        input_temp,
        input_wind_speed_min, input_wind_speed_avg,
        input_wind_speed_max, input_wind_direction,
        input_snowpack_height,input_1day_max_temp,
        input_1day_min_temp, input_2day_max_temp,
        input_2_day_min_temp,input_max_1_day_snow,
        input_2day_max_snow,input_3day_max_snow,
        input_precip]],
        columns = [
        'Temperature (deg F)',
        'Wind Speed Minimum (mph)', 'Wind Speed Average (mph)',
        'Wind Speed Maximum (mph)', 'Wind Direction (deg.)',
        'Total Snow Depth (in)', 'max_1_day_temp',
        'min_1_day_temp','max_2_day_temp',
        'min_2_day_temp', 'max_1_day_snow',
        'max_2_day_snow','max_3_day_snow',
        '4800_brooks'
        ])
    print(arguments.head())
    
    predicted = model.predict(arguments)[0]
    scaled_prediction = apply_scaling_factor(predicted)
    rounded_scaled_prediction = np.round(scaled_prediction,2)
    
    print(type(rounded_scaled_prediction))
    
    
    print((rounded_scaled_prediction), type(rounded_scaled_prediction))

    return jsonify({'Predicted Danger Level': rounded_scaled_prediction})
