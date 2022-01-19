from prophet.serialize import model_from_json
import json


def prophet_predict(start='1980', end='2000'):
    '''
    It is assumed start year will be greater then end year and values are ints
    or at least easily converted to ints 
    '''

    years = int(end) - int(start)
    with open('FBmodel.json', 'r') as fin:
        j = model_from_json(json.load(fin))

    future = j.make_future_dataframe(periods = years, freq='YS' )
    forecast = j.predict(future)

    forecast = forecast[['ds', 'yhat']]
    forecast['yhat'] = forecast['yhat'].astype(int)

    forecast_dict = dict()
    for index, dates in enumerate(forecast['ds']):
        if dates.month == 1 and dates.day == 1:
            forecast_dict[(dates.year)] = str(forecast['yhat'][index])


    return forecast_dict

