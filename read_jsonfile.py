from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
df_pyspark = spark.read.json("/home/niteesh/Pictures/jsons.json",multiLine=True)
df_pyspark.show(truncate=0)

