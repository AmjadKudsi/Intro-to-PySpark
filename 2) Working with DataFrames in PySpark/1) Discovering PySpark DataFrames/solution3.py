# print out their schemas instead of displaying the contents of each DataFrame

from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("BasicOperations").getOrCreate()

# Create a simple list of tuples representing data
data = [("Alice", 1), ("Bob", 2), ("Cathy", 1)]

# Create a DataFrame directly from the list
df_from_list = spark.createDataFrame(data, ["Name", "Value"])

# TODO: Change the following line to print the schema of the DataFrame
df_from_list.printSchema()

# Convert the list into an RDD
rdd = spark.sparkContext.parallelize(data)

# Create a DataFrame from the existing RDD
df_from_rdd = spark.createDataFrame(rdd, ["Name", "Value"])

# TODO: Change the following line to print the schema of the DataFrame
df_from_rdd.printSchema()

# Stop the SparkSession to release resources
spark.stop()