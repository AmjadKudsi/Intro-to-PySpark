# Modify the SQL query to calculate the average subscription period for each country

from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("AverageSubscriptionPeriod").getOrCreate()

# Load the customer dataset from a CSV file into a DataFrame
df = spark.read.csv("customers.csv", header=True, inferSchema=True)

# Convert DataFrame into a temporary view for SQL querying
df.createOrReplaceTempView("customers")

# TODO: Change the query to calculate the average subscription period for each country
query = """
SELECT Country, AVG(DATEDIFF(CURRENT_DATE, `Subscription Date`)) AS avg_subscription_period
FROM customers
GROUP BY Country
"""

# Execute the query
result_df = spark.sql(query)

# Display the execution plan for the query
result_df.explain()

# Show the results of the query
result_df.show()

# Stop the SparkSession to release resources
spark.stop()