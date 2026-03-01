# modify the map transformation with lambda x: x.capitalize() to capitalize each word in an RDD of strings

from pyspark.sql import SparkSession

# Initialize SparkSession for transformation operations
spark = SparkSession.builder \
    .master("local") \
    .appName("MapTransformation") \
    .getOrCreate()

# Create an RDD with string data
rdd = spark.sparkContext.parallelize(["pyspark", "transformations", "map", "rdd"])

# TODO: Change the map transformation to capitalize each word in the RDD
capitalized_rdd = rdd.map(lambda x: x.capitalize())

# Retrieve and print the transformed elements from the RDD
print("Capitalized words in the RDD:", capitalized_rdd.collect())

# Stop SparkSession to release resources
spark.stop()