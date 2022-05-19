from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

spark = SparkSession.builder.getOrCreate()
'''
#sparks drop empty rows
df=spark.read.csv('/home/niteesh/Music/spark_drop_empty_row.csv',header=True)
n=df.dropna()
n.repartition(1).write.mode('overwrite').format('csv').save('/home/niteesh/Music/spark_output_drop_empty_row.csv')
'''

'''
#droup duolicates
df=spark.read.csv('/home/niteesh/Documents/clean_data.csv',header= True, sep=',')
df.show()
#df.dropDuplicates().show(truncate=0)
df=df.dropDuplicates()
df.show()
df.repartition(1).write.mode('overwrite').format('csv').save('/home/niteesh/Music/output_drop_duplicates_in_spark')
'''


'''
#Filling Empty rows With NA
df=spark.read.csv('/home/niteesh/Music/cleaningup_data.csv')
df.na.fill('NA').show()
'''
'''
#Deleteing paticular column

df=spark.read.csv('/home/niteesh/Documents/delete_column.csv',header=True)
d=df.drop('age')

d.show()
'''
'''
#Selecting paticular column

df=spark.read.csv('/home/niteesh/Documents/delete_column.csv',header=True)
df.select('age').show()
'''
'''
#Drop coloumn
df=spark.read.csv('/home/niteesh/Videos/randm.csv',header=True)
df.drop(col('age')).show()
'''
'''
#Filling NA values with Thier Values
df=spark.read.csv('/home/niteesh/Music/filling_na_values_with_values.csv',header=True)
df.na.fill({'Name':'Raja','age':22}).show()
'''
'''
#Add new column with static data
df=spark.read.csv('/home/niteesh/Music/add_column.csv',header=True)
df.withColumn('lastname',lit('kumar')).show()
'''