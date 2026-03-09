# complete a SQL query to retrieve customer data based on a certain criterion

from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("SparkSQL").getOrCreate()

# Load the customer dataset from a CSV file into a DataFrame
df = spark.read.csv("customers.csv", header=True, inferSchema=True)

# TODO: Convert DataFrame into a temporary view to be used in SQL queries
df.createOrReplaceTempView("customers")

# TODO: Execute an SQL query to select customers based in a specific country, e.g., "Germany"
result_df = spark.sql("SELECT * FROM customers WHERE Country = 'Germany'")

# TODO: Display the result of the query
result_df.show()

# Stop the SparkSession to release resources
spark.stop()