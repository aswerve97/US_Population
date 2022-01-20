import prophet
import psycopg2
import pandas as pd
from secret import DATABASE_URL
con = psycopg2.connect(DATABASE_URL)
start_of_trainng = "1900"
### end would be the year the FORECASTS STARTS
end_of_training = "1910"
#training_years = int(start_of_trainng) - int(end_of_training)
projections_end = '1940'
year_range = int(projections_end) - int(end_of_training)

df = pd.read_sql(
f'''
SELECT
date_population AS DS,
population AS Y
FROM
us_population'''
    ,con = con)

m = prophet.Prophet(daily_seasonality=False, weekly_seasonality=False)
m.fit(df)

future = m.make_future_dataframe(periods = 1, freq='YS')
print(future)

#forecast = m.predict(future)
