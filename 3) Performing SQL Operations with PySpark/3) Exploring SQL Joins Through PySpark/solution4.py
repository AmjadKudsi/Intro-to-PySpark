# complete the code to execute a RIGHT JOIN

from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("SQLJoins").getOrCreate()

# Load the primary customer dataset
df1 = spark.read.csv("customers.csv", header=True, inferSchema=True)

# Load a second dataset containing additional customer details, such as purchase history
df2 = spark.read.csv("customer_purchase_history.csv", header=True, inferSchema=True)

# TODO: Convert df1 into a temporary view called "customers"
df1.createOrReplaceTempView('customers')

# TODO: Convert df2 into a temporary view called "purchase_history"
df2.createOrReplaceTempView('purchase_history')

# TODO:  Define a SQL RIGHT JOIN query to combine data based on the Customer Id
joined_query = """
SELECT c.*, p.PurchaseAmount
FROM customers c
RIGHT JOIN purchase_history p
ON c.`Customer Id` = p.`Customer Id`
"""

# TODO: Execute query
joined_df = spark.sql(joined_query)

# TODO: Display the joined DataFrame
joined_df.show()

# Stop the SparkSession to release resources
spark.stop()