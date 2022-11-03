import random
import decimal
from faker import Faker
import numpy as np
import pandas as pd

fake = Faker()

Daily_Miles = []
Daily_Kilometers = []
Daily_Miles_per_Hour = []
Daily_Kilometers_per_Hour = []

for i in range(365):
    Daily_Miles.append(float(random.randrange(100, 1200) / 100))
    Daily_Kilometers.append(float(random.randrange(100, 1200) / 100 * 0.62137119))
    Daily_Miles_per_Hour.append(float(random.randrange(100, 1200) / 100) / 60)
    Daily_Kilometers_per_Hour.append(float(random.randrange(100, 1200) / 100 * 0.62137119) / 60)

Daily_Income = []

for a in range(365):
    Daily_Income.append(float(random.randrange(1000, 1400) / 100))

Daily_Trip = []

for i in range(365):
    Daily_Trip.append(float(random.randrange(1, 8)))

Duration_Trip_Minutes = []

for i in range(365):
    Duration_Trip_Minutes.append(float(random.randrange(162, 181)))

print(Duration_Trip_Minutes)

fake_dataset_Uber = pd.DataFrame(
    {'Driver Name': Names, 'Daily Miles': Daily_Miles, 'Daily Kilometers': Daily_Kilometers,
     'Daily Miles per Hour': Daily_Miles_per_Hour
        , 'Daily Kilometers per Hour': Daily_Kilometers_per_Hour, 'Daily Income': Daily_Income, 'Daily Trip': Daily_Trip
        , 'Duration Trip Minutes': Duration_Trip_Minutes})

fake_dataset_Uber.to_csv('fake_dataset_Uber')

synthetic_data_Uber = pd.read_csv("fake_dataset_Uber.csv")
print(synthetic_data_Uber.head())

read_file = pd.read_csv(r'fake_dataset_Uber.csv')
read_file.to_excel(r'fake_dataset_Uber.xlsx', index=None, header=True)