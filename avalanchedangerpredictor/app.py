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

# Index(['Battery Voltage (v)', 'Temperature (deg F)',
    #    'Wind Speed Minimum (mph)', 'Wind Speed Average (mph)',
    #    'Wind Speed Maximum (mph)', 'Wind Direction (deg.)',
    #    'Total Snow Depth (in)', 'max_1_day_temp', 'min_1_day_temp',
    #    'max_2_day_temp', 'min_2_day_temp', 'max_1_day_snow', 'max_2_day_snow',
    #    'max_3_day_snow', '4800_brooks'],
    #   dtype='object')
    


      
               


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Return a random prediction."""
    """First lets see if it can return what I want"""
    data = request.json
    #prediction = model.predict_proba([data['user_input']])
    #return jsonify({'probability': prediction[0][1]})
    print(data)
    input_solar_text = data['input_solar_01']
    print(input_solar_text, type(input_solar_text))
    input_solar = float(input_solar_text)
    
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
    input_1day_min_temp = float(input_1day_min_temp)
    
    input_2day_max_temp_text = data['input_2day_max_temp_10']
    input_2day_max_temp = float(input_2day_max_temp_text)
    
    input_2_day_min_temp_text = data['input_2_day_min_temp_11']
    input_2_day_min_temp = float(input_2_day_min_temp_text)
    
    input_1day_max_snow_text = data['input_1day_max_snow_12']
    input_max_1_day = float(input_1day_max_snow_text)
    
    input_2day_max_snow_text = data['input_2day_max_snow_13']
    input_2day_max_snow = float(input_2day_max_snow_text)
    
    input_3day_max_snow_14_text = data['input_3day_max_snow_14']
    input_3day_max_snow_14 = float(input_3day_max_snow_14_text)
    
    input_precip_text = data['input_precip_15']
    input_precip = float(input_precip_text)
    
    
    arguments = pd.DataFrame(
        [[solar_input, temp_input,input_min_wind_speed,
        input_wind_direction,input_total_snow_depth, input_max_1_day_temp,
        input_max_2_day_temp, input_max_1_day_snow, input_max_2_day_snow,
        input_max_3_day_snow, input_precipitation]],
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
