import prophet
import psycopg2
import pandas as pd
from secret import DATABASE_URL
con = psycopg2.connect(DATABASE_URL)
start_of_trainng = "1900"
### end would be the year the FORECASTS STARTS
end_of_training = "1910"
projections_end = '1940'
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
	#if dates.year >= start and dates.year <= end and dates.month == 1 and dates.day == 1:
	    
print(forecast_dict)