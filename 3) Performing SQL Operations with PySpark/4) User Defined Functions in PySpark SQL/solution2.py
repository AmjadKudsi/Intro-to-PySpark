# fixing bugs 

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("UDFunction").getOrCreate()

# Load the customer dataset from a CSV file into a DataFrame
df = spark.read.csv("customers.csv", header=True, inferSchema=True)

# Create a temporary view of the DataFrame
df.createOrReplaceTempView("customers")

# Define a UDF that formats the customer's name in uppercase
def format_name(name):
    return name.upper()

# Convert the Python function to a PySpark UDF
format_name_udf = udf(format_name, StringType())

# Register the UDF with Spark
spark.udf.register("format_name_udf", format_name_udf)

# Define the SQL query using the UDF
query = """
SELECT format_name_udf(`First Name`) AS FormattedName, `Last Name`
FROM customers
"""

# Use the query to format customer names
result_df = spark.sql(query)

# Display the formatted result
result_df.show()

# Stop the SparkSession to release resources
spark.stop()