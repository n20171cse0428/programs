from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df_pyspark = spark.read.csv("/home/niteesh/Music/sparks_readcsv.csv",header=True)
df_pyspark.show(truncate=0)
