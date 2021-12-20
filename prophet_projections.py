import pandas as pd
from prophet import Prophet

years = 20


df = pd.read_csv('population_data_pre_1981.csv')
df.columns = ['y', 'ds']
m = Prophet(daily_seasonality=False, weekly_seasonality=False)
m.fit(df)
future = m.make_future_dataframe(periods=int(365.25 * years))
forecast = m.predict(future)



forecast['yhat'] = forecast['yhat'] 
forecast.to_csv('data.csv', index_label=False, columns=['ds', 'yhat'])
