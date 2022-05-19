from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.types import StructType, ArrayType, StringType, IntegerType

spark = SparkSession.builder.getOrCreate()
schema = StructType().add('people',ArrayType(StructType().add('firstName',StringType()).add('lastName',StringType()).add('gender',StringType()).add('age',IntegerType()).add('number',StringType())))
df=spark.read.option('multiline','true').json('/home/niteesh/Videos/schema.json',schema=schema)
df=df.withColumn('exploded',explode(df['people']))
df = df.select(df['exploded'])
df.show(truncate=0)
