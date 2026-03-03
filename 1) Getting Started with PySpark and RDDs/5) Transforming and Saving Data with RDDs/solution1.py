# insert the correct function name to save the extracted product names from the high-value sales

from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .master("local") \
    .appName("SalesDataProcessing") \
    .getOrCreate()

# Create an RDD by reading from a sales data file
sales_rdd = spark.sparkContext.textFile("sales.txt")

# Use filter to retain only sales entries with amounts greater than $100
high_value_sales_rdd = sales_rdd.filter(lambda line: float(line.split(",")[1]) > 100)

# Use map to extract product names from high value sales, assuming format: "Product,Amount"
product_names_rdd = high_value_sales_rdd.map(lambda line: line.split(",")[0])

# TODO: Save the extracted product names
product_names_rdd.saveAsTextFile("output_products")

# Read the content of the saved files
saved_rdd = spark.sparkContext.textFile("output_products")

# Collect and print the first three products
print(saved_rdd.take(3))

# Stop SparkSession to release resources
spark.stop()