# Change the filter condition so that the RDD retains only odd numbers

from pyspark.sql import SparkSession

# Initialize SparkSession to perform filter operations
spark = SparkSession.builder \
    .master("local") \
    .appName("FilterTransformation") \
    .getOrCreate()

# Create an RDD for applying filter transformations
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])

# TODO: Change the filter condition to retain only odd numbers and update the rdd name
odd_rdd = rdd.filter(lambda x: x % 2 != 0)

# TODO: Update the print statement to reflect the new operation
print("Odd elements in the RDD:", odd_rdd.collect())

# Stop SparkSession to release resources
spark.stop()