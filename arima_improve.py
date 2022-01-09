import pickle
import pandas as pd

with open('model.pkl', 'rb') as file:
    arima_model = pickle.load(file)

start = '1980'
end = '1990'

forecast = arima_model.get_prediction(start, end)
arima_value_forecast = forecast.predicted_mean

df = arima_value_forecast.to_frame()


