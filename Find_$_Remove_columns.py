# large_csv_prosessing
#Find_$_Remove_columns_large_csv

'''
import csv

# Read the CSV file
with open('#target.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# Find blank columns
blank_cols = []
for i in range(len(data[0])):
    col_data = [row[i] for row in data]
    if all(val == '' for val in col_data):
        blank_cols.append(i)

# Print the indices of blank columns
print(blank_cols)
'''

import csv

# Read the CSV file
with open('#target.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# Find blank columns
blank_cols = []
for i in range(len(data[0])):
    col_data = [row[i] for row in data]
    if all(val == '' for val in col_data):
        blank_cols.append(i)

# Remove blank columns
for row in data:
    for i in sorted(blank_cols, reverse=True):
        del row[i]

# Write the modified data to a new CSV file
with open('#output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
