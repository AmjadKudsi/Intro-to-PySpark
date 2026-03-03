# fill in the missing parts to create a complete process

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

# TODO: Save the extracted product names to "output_products"
product_names_rdd.saveAsTextFile("output_products")


# TODO: Read the content of the saved directory
saved_rdd = spark.sparkContext.textFile("output_products")


# TODO: Collect and print the first five products
print(saved_rdd.take(5))


# Stop SparkSession to release resources
spark.stop()