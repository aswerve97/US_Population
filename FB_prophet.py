import prophet
import psycopg2
import pandas as pd
from secret import DATABASE_URL
con = psycopg2.connect(DATABASE_URL)

def prophet_predict(start=1980, end=2000):
    '''
    It is assumed start year will be greater then end year and values are ints
    or at least easily converted to ints 
    '''
    start_of_trainng = 1900
    #we want our our training model to not consider any data after this date
    end_of_training = start
    projections_end = end
    year_range = int(projections_end) - int(end_of_training)

    df = pd.read_sql(
    f'''
    SELECT 
    *
    FROM
    (
    SELECT
        date_population AS DS,
        population AS Y
    FROM
    us_population) as sub
    WHERE
    DS >='{start_of_trainng}-01-01' AND DS <='{end_of_training}-01-01' ''',
    con = con
    )

    m = prophet.Prophet(daily_seasonality=False, weekly_seasonality=False)
    m.fit(df)

    future = m.make_future_dataframe(periods = year_range, freq='YS')
    forecast = m.predict(future)

    forecast['yhat'] = forecast['yhat'].astype(int)

    forecast_dict = dict()
    for index, dates in enumerate(forecast['ds']):
        forecast_dict[(dates.year)] = str(forecast['yhat'][index])


    return forecast_dict

