# Define an SQL query to calculate the average number of customers across all countries
# Utilize a subquery by enclosing it in parentheses to first count the number of customers for each country. Use this subquery as a derived table to then calculate the overall average
# Execute the defined SQL query using the temporary SQL view
# Display the execution plan for the SQL query to understand its behavior
# Show the results obtained from the query execution

from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("UnderstandingSQLQueries").getOrCreate()

# Load the customer dataset from a CSV file into a DataFrame
df = spark.read.csv("customers.csv", header=True, inferSchema=True)

# Convert DataFrame into a temporary view for SQL querying
df.createOrReplaceTempView("customers")

# TODO: Define an SQL query to calculate the average number of customers across all countries
query = """
SELECT AVG(tot_customers) AS avg_customers FROM (
    SELECT Country, COUNT(`Customer ID`) AS tot_customers FROM customers
    GROUP BY Country
) C
"""

# TODO: Execute the query
result_df = spark.sql(query)

# TODO: Display the execution plan for the query
result_df.explain()

# TODO: Show the results of the query
result_df.show()

# Stop the SparkSession to release resources
spark.stop()