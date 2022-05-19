import pandas as pd
'''
df = pd.read_csv('/home/niteesh/Pictures/rm_duplicates.csv')
print(df.drop_duplicates('name',inplace=True))

print(df.to_csv('/home/niteesh/Pictures/output_rm_duplicates.csv',index=False))
'''


'''
df = pd.read_csv('/home/niteesh/Pictures/rename_colum.csv')
df.rename(columns={'place':'address'},inplace=True)
print(df.to_csv('/home/niteesh/Pictures/output_rename.csv'))
'''
'''
df = pd.read_csv('/home/niteesh/Pictures/add_column.csv')
df['place']=["banglore","hydrabad","anantapur"]
print(df.to_csv('/home/niteesh/Pictures/output_add_column.csv'))
'''
'''
df = pd.read_csv("/home/niteesh/Pictures/drop_column.csv")
df.drop(columns='name')
print(df.to_csv('/home/niteesh/Pictures/output_drop_column.csv'))
'''
'''
df = pd.read_csv("/home/niteesh/Pictures/select_column.csv")

print(df['place'].to_csv('/home/niteesh/Pictures/output_select_column.csv'))
'''
