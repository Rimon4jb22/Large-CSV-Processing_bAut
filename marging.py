# marging_large_csv_files

import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('#1st.csv')

# Read the second CSV file
df2 = pd.read_csv('#2nd.csv')

# Merge the two dataframes based on a common column
merged_df = pd.concat([df1, df2], axis=0)

# Write the merged dataframe to a new CSV file
merged_df.to_csv('#output.csv', index=False)
