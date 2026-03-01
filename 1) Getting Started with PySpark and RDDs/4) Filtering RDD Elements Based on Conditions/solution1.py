# complete the code snippet that filters even numbers from a list 

from pyspark.sql import SparkSession

# Initialize SparkSession to perform filter operations
spark = SparkSession.builder \
    .master("local") \
    .appName("FilterTransformation") \
    .getOrCreate()

# Create an RDD for applying filter transformations
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])

# TODO: Filter the RDD to retain only even numbers using a lambda function
even_rdd = rdd.filter(lambda x: x % 2 == 0)

# Retrieve and print the filtered elements from the RDD
print("Even elements in the RDD:", even_rdd.collect())

# Stop SparkSession to release resources
spark.stop()