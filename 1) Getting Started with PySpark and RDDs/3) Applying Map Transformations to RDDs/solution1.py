# complete the code snippet where you apply a map transformation to an RDD and collect the results

from pyspark.sql import SparkSession

# Initialize SparkSession for transformation operations
spark = SparkSession.builder \
    .master("local") \
    .appName("MapTransformation") \
    .getOrCreate()

# Create an RDD as the basis for transformation
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])

# TODO: Apply a map transformation to square each element in the RDD
squared_rdd = rdd.map(lambda x: x ** 2)

# TODO: Retrieve and print the transformed elements from the RDD
print("Elements squared in the RDD:", squared_rdd.collect())

# Stop SparkSession to release resources
spark.stop()