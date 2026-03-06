# Follow the intstructions

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("BasicOperations").getOrCreate()

# Load a DataFrame from a CSV file with headers
df = spark.read.csv("employees.csv", header=True, inferSchema=True)

# TODO: Select the columns "Department" and "Salary" from the DataFrame
selected_df = df.select("Department", "Salary")

# TODO: Filter out the rows where Salary is below 3500
filtered_df = selected_df.filter(selected_df.Salary > 3500)

# TODO: Update the "Salary" column by adding 1000 to each value
updated_df = filtered_df.withColumn("Salary", col("Salary") + 1000)

# TODO: Add a new column "Bonus" that is 10% of the updated salary
added_df = updated_df.withColumn("Bonus", col("Salary") * 0.10)

# TODO: Show the final DataFrame with the updated and added columns
added_df.show()

# Stop the SparkSession to release resources
spark.stop()