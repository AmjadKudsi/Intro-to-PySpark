# tweak some operations to see how it changes the outcome

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("BasicOperations").getOrCreate()

# Load a DataFrame from a CSV file with headers
df = spark.read.csv("employees.csv", header=True, inferSchema=True)

# Select specific columns
selected_df = df.select("Name", "Salary")

# TODO: Change the filter condition to a different salary value
filtered_df = selected_df.filter(df.Salary % 1000 == 0)

# TODO: Change the salary update value
updated_df = filtered_df.withColumn("Salary", col("Salary") + 1000)

# TODO: Rename the new column from "Bonus" to "Extra"
added_df = updated_df.withColumn("Bonus", col("Salary") * 0.5)

# Display final DataFrame
added_df.show()

# Stop the SparkSession to release resources
spark.stop()