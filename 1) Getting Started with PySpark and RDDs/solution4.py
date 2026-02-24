# write the complete code sequence from scratch

from pyspark.sql import SparkSession

# TODO: Initialize SparkSession to interface with Spark
# - Set master as "local" to run Spark locally
# - Set appName as "GettingStarted"
# - Retrieve an existing SparkSession or create a new one
spark = SparkSession.builder \
        .master("local") \
        .appName("GettingStarted") \
        .getOrCreate()

# TODO: Define a simple list of numbers as input data
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TODO: Convert the list into an RDD
nums_rdd = spark.sparkContext.parallelize(nums)

# TODO: Retrieve and print all elements from the RDD collection
print("All elements in the RDD: ", nums_rdd.collect())

# TODO: Stop SparkSession to release resources
spark.stop()