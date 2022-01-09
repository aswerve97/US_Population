import pickle

with open("arima121model.pkl", "rb") as file:
    arima_model = pickle.load(file)


def arima_predict(start="1980", end="1990"):

    forecast = arima_model.get_prediction(start, end)
    arima_value_forecast = forecast.predicted_mean

    year = []
    fc = []
    for date in forecast.row_labels:
        year.append(str(date)[:4])
    for value in arima_value_forecast:
        fc.append(int(value))
    result = zip(year, fc)

    forecast_dict = dict()

    for year, value in result:
        forecast_dict[year] = value

    return forecast_dict
