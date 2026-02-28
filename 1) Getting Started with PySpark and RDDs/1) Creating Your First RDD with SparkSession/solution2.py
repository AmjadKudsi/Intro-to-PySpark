# tweak the configuration to utilize all available cores on your local machine

from pyspark.sql import SparkSession

# TODO: Change master to utilize all cores on local machine
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("GettingStarted") \
    .getOrCreate()

# Define a simple list of numbers as input data
nums = [1, 2, 3, 4, 5]

# Convert the list into an RDD (Resilient Distributed Dataset)
nums_rdd = spark.sparkContext.parallelize(nums)

# Retrieve and print all elements from the RDD collection
print("All elements in the RDD:", nums_rdd.collect())

# Stop SparkSession to release resources
spark.stop()