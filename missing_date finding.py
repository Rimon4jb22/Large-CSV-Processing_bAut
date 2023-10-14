# missing_date_from_large_csv

import csv
from datetime import datetime
import pandas as pd

# Read the CSV file and extract the date column
dates = []
with open('#target.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # skip the header row
    dates = [datetime.strptime(column [0], '%d-%B-%Y') for column  in csv_reader]

# Generate a list of all dates in the range
all_dates = pd.date_range(min(dates), max(dates), freq='D').strftime('%d-%B-%Y').tolist()

# Find the missing dates
missing_dates = set(all_dates) - set([date.strftime('%d-%B-%Y') for date in dates])

print(all_dates)

print(missing_dates)

# Write the missing dates to a new CSV file
with open('#output.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for date in missing_dates:
        csv_writer.writerow([date])
