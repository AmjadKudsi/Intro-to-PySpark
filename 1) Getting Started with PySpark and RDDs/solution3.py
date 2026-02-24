# Transform a list into an RDD and use the correct method to retrieve

from pyspark.sql import SparkSession

# Initialize SparkSession to interface with Spark
spark = SparkSession.builder \
    .master("local") \
    .appName("GettingStarted") \
    .getOrCreate()

# Define a simple list of numbers as input data
nums = [1, 2, 3, 4, 5]

# TODO: Convert the list into an RDD (Resilient Distributed Dataset)
nums_rdd = spark.sparkContext.parallelize(nums)

# TODO: Retrieve and print all elements from the RDD collection
print("All the elements in the RDD: ", nums_rdd.collect())

# Stop SparkSession to release resources
spark.stop()