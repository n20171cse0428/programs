


from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
df=spark.read.json('/home/niteesh/Music/spark_input_jsonfile.json',header=True)
df.repartition(1).write.mode('overwrite').format('csv').save('/home/niteesh/Music/sparks_output_csvfile.csv')
