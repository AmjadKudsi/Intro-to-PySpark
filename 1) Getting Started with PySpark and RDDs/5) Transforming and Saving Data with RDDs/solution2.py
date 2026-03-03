# Change the reading pattern in the PySpark script to read a specific partition by using the exact file name

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

# Save the extracted product names to a new text file
product_names_rdd.saveAsTextFile("output_products")

# TODO: Change the line to read only the first partition of saved RDD
saved_rdd = spark.sparkContext.textFile("output_products/part-00000")

# Collect and print the first three products from the first partition
print(saved_rdd.take(3))

# Stop SparkSession to release resources
spark.stop()