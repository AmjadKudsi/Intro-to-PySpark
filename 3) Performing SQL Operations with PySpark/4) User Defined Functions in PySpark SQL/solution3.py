from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("UDFunction").getOrCreate()

# Load the customer dataset from a CSV file into a DataFrame
df = spark.read.csv("customers.csv", header=True, inferSchema=True)

# Create a temporary view of the DataFrame
df.createOrReplaceTempView("customers")

# TODO: Change the UDF to count the length of the customer's email using the len() method
#  - Name the function as email_length
def email_length(mail):
    return len(mail)

# TODO: Convert the 'email_length' function to a PySpark UDF using IntegerType
# - Name the udf as email_length_udf
email_length_udf = udf(email_length, IntegerType())

# TODO: Register the email_length_udf UDF with Spark as "email_length_udf"
spark.udf.register("email_length_udf", email_length_udf)

# TODO: Modify the query to calculate email lengths using email_length_udf'
query = """
SELECT Email, email_length_udf(`Email`) AS email_length
FROM customers
"""

# Execute the query
result_df = spark.sql(query)

# Display the result
result_df.show()

# Stop the SparkSession to release resources
spark.stop()