# modify the existing code to drop only the rows where the "Age" is missing

from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("HandlingMissingValues").getOrCreate()

# Load a DataFrame from a CSV file with some missing values
df = spark.read.csv("students.csv", header=True, inferSchema=True)

# Fill missing values with specified default values
df_fill = df.fillna({"Name": "Unknown", "Score": 0})

# Show the DataFrame after filling missing values
df_fill.show()

# TODO: Change the dropna method to only drop rows with missing 'Age' values
df_drop = df_fill.dropna(subset=['Age'])

# Display the DataFrame after dropping rows with missing values
df_drop.show()

# Stop the SparkSession to release resources
spark.stop()