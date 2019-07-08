import random
import pandas as pd
from sklearn.pipeline import Pipeline
import pickle
from flask import Flask, request, render_template, jsonify


with open('avy_danger_prediction.pkl', 'rb') as f:
    model = pickle.load(f)
app = Flask(__name__, static_url_path="")

@app.route('/')
def index():
    """Return the main page."""
    return render_template('index.html')

# 'Battery Voltage (v)', 'Temperature (deg F)',
#        'Wind Speed Minimum (mph)', 'Wind Speed Average (mph)',
#        'Wind Speed Maximum (mph)', 'Wind Direction (deg.)',
#        '24 Hour Snow (in)', 'Total Snow Depth (in)', 'max_1_day_temp',
#        'min_1_day_temp', 'max_2_day_temp', 'min_2_day_temp', 'max_1_day_snow',
#        'max_2_day_snow', 'max_3_day_snow', '4800_brooks'
    
    


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Return a random prediction."""
    """First lets see if it can return what I want"""
    data = request.json
    #prediction = model.predict_proba([data['user_input']])
    #return jsonify({'probability': prediction[0][1]})
    print(data)
    
    solar_input_text = document['input_solar_1']
    print(hour_24_text, type(hour_24_text))
    solar_input = int(solar_input_text)
    
    temp_input_text = document['input_temp_2']
    temp_input = int(temp_input)
    
    input_min_wind_speed_text = document['input_wind_speed_min_3']
    input_min_wind_speed = int(input_min_wind_speed_text)
    
    input_wind_direction_text = document['input_wind_direction_4']
    input_wind_direction = int(input_min_wind_speed_text)
    
    
    input_total_snow_depth_text = document['input_total_snow_depth_5']
    input_total_snow_depth = int(input_total_snow_depth_text)
    
    
    input_max_1_day_temp_text = document['input_max_1_day_temp_6']
    input_max_1_day_temp = int(input_max_1_day_temp_text)
    
    
    input_max_2_day_temp_text = document['input_max_2_day_temp_7']
    input_max_2_day_temp = int(input_max_2_day_temp_text)
    
    
    input_max_1_day_snow_text = document['input_max_1_day_snow_8']
    input_max_1_day_snow = int(input_max_1_day_snow_text)
    
    
    input_max_2_day_snow_text = document['input_max_2_day_snow_9']
    input_max_2_day_snow = int(input_max_2_day_snow_text)
    
    
    input_max_3_day_snow_text = document['input_max_3_day_snow_10']
    input_max_3_day_snow = int(input_max_3_day_snow_text)
    
    
    input_precipitation_text = document['input_precipitation_11']
    input_precipitation = int(input_precipitation_text)
    
    
    arguments = pd.DataFrame(
        [[solar_input, temp_input,input_min_wind_speed,
                 input_wind_direction,input_total_snow_depth, input_max_1_day_temp,
                 input_max_2_day_temp, input_max_1_day_snow, input_max_2_day_snow,
                 input_max_3_day_snow, input_precipitation]].
        columns = ['Battery Voltage (v)', 'Temperature (deg F)','Wind Speed Minimum (mph)', 
         'Wind Speed Average (mph)','Wind Speed Maximum (mph)',
         'Wind Direction (deg.)','24 Hour Snow (in)', 'Total Snow Depth (in)',
         'max_1_day_temp','min_1_day_temp', 'max_2_day_temp',
         'min_2_day_temp','max_1_day_snow','max_2_day_snow', 
         'max_3_day_snow', '4800_brooks']
    )
    
    
    
    # prediction = model.predict_proba([data['user_input']])
    
    predicted_score = model.predict(arguments)
    rounded_predicted_score = round(predicted_score)

    return jsonify({'Avalanche Danger Level': rounded_predicted_score})