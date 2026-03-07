# Change the default value for missing "Name" entries from "Unknown" to "Student"
# Set a default value for missing "Country" entries to "Not Provided"

from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("HandlingMissingValues").getOrCreate()

# Load a DataFrame from a CSV file with some missing values
df = spark.read.csv("students.csv", header=True, inferSchema=True)

# TODO: Set the default value for:
# - Missing "Name" entries to "Student" instead of "Unknown"
# - Missing "Country" entries to "Not Provided"
df_fill = df.fillna({"Name": "Student", "Score": 0, "Country": "Not Provided"})

# Show the DataFrame after filling missing values
df_fill.show()

# Drop rows from the DataFrame that contain any null values
df_drop = df_fill.dropna()

# Display the DataFrame after dropping rows with missing values
df_drop.show()

# Stop the SparkSession to release resources
spark.stop()