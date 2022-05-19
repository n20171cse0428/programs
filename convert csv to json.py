import pandas as pd
df = pd.read_csv ('/home/niteesh/Pictures/csv_to_json.csv')
df.to_json ('/home/niteesh/Pictures/out_jsonfile.json')
