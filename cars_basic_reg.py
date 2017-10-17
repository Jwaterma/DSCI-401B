import pandas as pd
import pprint

cars = pd.read_csv('./data/cars.csv.')

# Nicely prints out the first few rows of data (head() gets first few rows)
pprint.pprint(cars.head())

# Show column names
print(list(cars))