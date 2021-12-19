import pickle
import pandas as pd
import json 


with open('model.pkl', 'rb') as file:
    arima_model = pickle.load(file)

def predict(start = '1980', end = '1990'):

    forecast = arima_model.get_prediction( start , end )
    arima_value_forecast = forecast.predicted_mean

    year = []
    fc = []
    for date in forecast.row_labels:
        year.append(str(date)[:4])
    for value in arima_value_forecast:
        fc.append(int(value))
    result = zip(year, fc)

    forecast_dict = dict()

    for year,value in result:
        forecast_dict[year] = value

    #json_object = json.dumps(forecast_dict, indent = 4) 

    return forecast_dict