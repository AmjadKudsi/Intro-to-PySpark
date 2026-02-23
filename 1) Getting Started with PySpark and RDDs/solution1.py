# fill in the missing code to build a SparkSession, transform a list into an RDD, retrieve its elements, and close the session

from pyspark.sql import SparkSession

# Initialize SparkSession to interface with Spark
# - Use the builder method to start building a SparkSession
# - Set master to local to run Spark locally
# - Set the application name using appName()
# - Create or get SparkSession with getOrCreate()
spark = SparkSession.builder \
    .master("local") \
    .appName("GettingStarted") \
    .getOrCreate()

# Define a simple list of numbers as input data
nums = [1, 2, 3, 4, 5]

# TODO: Convert the list into an RDD (Resilient Distributed Dataset)
nums_rdd = spark.sparkContext.parallelize(nums)

# TODO: Retrieve and print all elements from the RDD collection
print("All elements in the RDD:", nums_rdd.collect())

# TODO: Stop SparkSession to release resources
spark.stop()