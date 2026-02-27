# complete the script by filling in the missing parts for the following operations

from pyspark.sql import SparkSession

# Initialize SparkSession for file operations
spark = SparkSession.builder \
    .master("local") \
    .appName("LoadingFiles") \
    .getOrCreate()

# Create an RDD by reading data from a text file
file_rdd = spark.sparkContext.textFile("data.txt")

# TODO: Retrieve and print the first 4 lines from the RDD
print("First 4 lines from the RDD: ", file_rdd.take(4))


# TODO: Count and print the total number of lines in the RDD
print("Total number of lines in the RDD: ", file_rdd.count())


# TODO: Retrieve and print the first line of the RDD
print("First line in the RDD: ", file_rdd.first())


# Stop SparkSession to release resources
spark.stop()