from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df_pyspark = spark.read.csv("/home/niteesh/Music/sparks_readcsv.csv",header=True)
df_pyspark.repartition(1).write.mode('overwrite').format('json').save('/home/niteesh/Music/sparks_output_json.json')