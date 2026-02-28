# ensure that the data.csv file is correctly loaded into an RDD and perform a series of operations on it

from pyspark.sql import SparkSession

# Initialize SparkSession for file operations
spark = SparkSession.builder \
    .master("local") \
    .appName("LoadingFiles") \
    .getOrCreate()

# Create an RDD by reading data from a csv file
file_rdd = spark.sparkContext.textFile("data.csv")

# Retrieve and print the first 3 lines from the RDD
print("First 3 elements of the RDD:", file_rdd.take(3))

# Count and print the total number of lines in the RDD
print("Total number of lines in the RDD:", file_rdd.count())

# Retrieve and print the first line in the RDD
print("First line in the RDD:", file_rdd.first())

# Stop SparkSession to release resources
spark.stop()