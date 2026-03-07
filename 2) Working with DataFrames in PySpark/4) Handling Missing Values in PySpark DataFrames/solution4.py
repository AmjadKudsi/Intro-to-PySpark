# Complete the code

from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("HandlingMissingValues").getOrCreate()

# Load a DataFrame from a CSV file with some missing values
df = spark.read.csv("students.csv", header=True, inferSchema=True)

# TODO: Fill missing "Name" values with "Unknown", and "Country" values with "Not Specified"
df_fill = df.fillna({"Name": "Unknown", "Country": "Not Specified"})

# TODO: Display the DataFrame after filling missing values
df_fill.show()

# TODO: Drop rows with any missing values from the filled DataFrame
df_drop = df_fill.dropna()

# TODO: Display the DataFrame after dropping rows
df_drop.show()

# Stop the SparkSession to release resources
spark.stop()