# Modify the code to combine the separate DataFrame operations into a single chained operation

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("BasicOperations").getOrCreate()

# Load a DataFrame from a CSV file with headers
df = spark.read.csv("employees.csv", header=True, inferSchema=True)

# Select specific columns
df = df.select("Name", "Salary") \
       .filter(df.Salary > 2500) \
       .withColumn("Salary", col("Salary") + 300) \
       .withColumn("Bonus", col("Salary") * 0.1)

# Display final DataFrame
df.show()

# Stop the SparkSession to release resources
spark.stop()