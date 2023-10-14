#keyword_count_from_large_csv

import csv


# List of keywords to search for
keywords = [
    "Banker",
    "Businessman",
    "Doctor",
    "Engineer",
    "Government-Employees",
    "Health-Worker",
    "Journalist",
    "Midwife",
    "Non-Government-Employees",
    "Others",
    "Self-employment",
    "Senior-Staff-Nurse/Staff-Nurse",
    "Student",
    "Teacher"
]

# Dictionary to store keyword counts for each date
keyword_counts = {}

# Read CSV file and iterate over rows
with open('#target.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader) # Skip header row
    date_index = headers.index('date') # Index of Date column
    for row in reader:
        date = row[date_index]
        # Initialize count dictionary for current date
        if date not in keyword_counts:
            keyword_counts[date] = {k: 0 for k in keywords}
        # Increment count for each keyword in current row
        for keyword in keywords:
            if keyword.lower() in row:
                keyword_counts[date][keyword] += 1

# Print keyword counts for each date
for date, counts in keyword_counts.items():
    print("Date:", date)
    for keyword, count in counts.items():
        print(keyword, count)
