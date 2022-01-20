import psycopg2
import pandas as pd
from secret import DATABASE_URL
con = psycopg2.connect(DATABASE_URL)
data = pd.read_sql('SELECT * FROM us_population', con = con)

print(data)

