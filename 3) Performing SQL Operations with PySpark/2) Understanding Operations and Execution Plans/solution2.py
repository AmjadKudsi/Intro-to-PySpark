#change the data source loading from a CSV file to a Parquet file

from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("UnderstandingSQLQueries").getOrCreate()

# TODO: Change this line to read from a Parquet file instead
df = spark.read.parquet("customers.parquet", header=True, inferSchema=True)

# Convert DataFrame into a temporary view for SQL querying
df.createOrReplaceTempView("customers")

# Define an SQL query to count the number of customers from each country
query = """
SELECT Country, COUNT(*) as CustomerCount
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