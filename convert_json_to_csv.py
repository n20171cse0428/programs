import pandas as pd
df = pd.read_json ('/home/niteesh/Pictures/jsons.json')
df.to_csv ('/home/niteesh/Pictures/output_csvfile.csv')
print(df)