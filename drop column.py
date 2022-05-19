

import pandas as pd

df = pd.read_csv('/home/niteesh/Pictures/csv2.csv')

n=df.dropna()

n.to_csv('/home/niteesh/Pictures/drop_empty_colums.csv',index=False)