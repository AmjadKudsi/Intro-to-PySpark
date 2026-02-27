# Use textFile to read data from "employees.csv" into an RDD

from pyspark.sql import SparkSession

# Initialize SparkSession for file operations
spark = SparkSession.builder \
    .master("local") \
    .appName("LoadingFiles") \
    .getOrCreate()

# TODO: Create an RDD by reading data from a CSV file named "employees.csv"
file_rdd = spark.sparkContext.textFile("employees.csv")

# TODO: Retrieve and print the first 10 elements from the RDD
print("First 10 elements from the RDD: ", file_rdd.take(10))

# TODO: Count and print the total number of lines in the RDD
print("Total number of lines in the RDD: ", file_rdd.count())

# TODO: Retrieve and print the first line of the RDD
print("First line of the RDD: ", file_rdd.first())

# TODO: Stop SparkSession to release resources
spark.stop()