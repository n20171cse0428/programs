import pandas as pd

df = pd.read_csv('/home/niteesh/Pictures/csv3.csv')

df.fillna(99, inplace = True)

print(df.to_csv('/home/niteesh/Pictures/replaces_null_rows_values.csv',index=False))


