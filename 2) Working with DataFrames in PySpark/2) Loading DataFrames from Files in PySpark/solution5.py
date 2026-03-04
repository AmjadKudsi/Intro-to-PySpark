# fill in the missing parts of the code to load data from CSV, JSON, and Parquet files into DataFrames

from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("LoadingDataFrames").getOrCreate()

# TODO: Load a DataFrame from a CSV file at 'data.csv' with headers and schema inference
csv_df = spark.read.csv("data.csv", header=True, inferSchema=True)

# TODO: Display the first 3 rows of the CSV DataFrame
csv_df.show(3)

# TODO: Load a DataFrame from a JSON file at 'data.json'
json_df = spark.read.json("data.json")

# TODO: Display the first 3 rows of the JSON DataFrame
json_df.show(3)

# TODO: Load a DataFrame from a Parquet file at 'data.parquet'
parquet_df = spark.read.parquet("data.parquet")

# TODO: Display the first 3 rows of the Parquet DataFrame
parquet_df.show(3)

# Stop the SparkSession to release resources
spark.stop()