import pandas as pd
from pyhive import hive

cursor = hive.connect(host='localhost', port='10000').cursor()

cursor.execute('select * from pokes')
data = pd.DataFrame(cursor.fetchall())
print(data.head())
