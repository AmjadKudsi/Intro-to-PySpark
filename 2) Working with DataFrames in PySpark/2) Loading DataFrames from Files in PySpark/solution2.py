# change the CSV loading option from header=True to header=False and observe how this change

from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("LoadingDataFrames").getOrCreate()

# TODO: Change the header option to False in the CSV loading
csv_df = spark.read.csv("data.csv", header=False, inferSchema=True)

# Display the inferred schema of the CSV DataFrame
csv_df.printSchema()

# Display the first 3 rows of the CSV DataFrame
csv_df.show(3)

# Stop the SparkSession to release resources
spark.stop()