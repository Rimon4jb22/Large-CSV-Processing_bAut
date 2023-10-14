# auto sum script for large csv...

import pandas as pd


df = pd.read_csv(' #the_csvfile_need_to_work_on ')

# Get a list of the columns that end with ".#target_key "
banker_cols = [col for col in df.columns if col.endswith('.Banker')]  #as_example


# new column with the merged values
df['Banker_combined'] = df[banker_cols].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)  #as_example


# sum of the ".#target " columns
df['Banker'] = df[banker_cols].sum(axis=1, skipna=True) #as_example

df = df.drop(banker_cols, axis=1)

df.to_csv('#name_of_the_output.csv', index=False)
