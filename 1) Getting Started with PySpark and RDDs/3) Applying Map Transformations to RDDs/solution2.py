# modify the lambda function inside the map transformation to cube each element instead of squaring

from pyspark.sql import SparkSession

# Initialize SparkSession for transformation operations
spark = SparkSession.builder \
    .master("local") \
    .appName("MapTransformation") \
    .getOrCreate()

# Create an RDD as the basis for transformation
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])

# TODO: Change the lambda function to cube each element in the RDD
cubed_rdd = rdd.map(lambda x: x ** 3)

# TODO: Update the print statement to reflect cubed elements
print("Elements cubed in the RDD:", cubed_rdd.collect())

# Stop SparkSession to release resources
spark.stop()