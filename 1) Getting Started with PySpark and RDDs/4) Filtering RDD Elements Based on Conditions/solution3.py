# update the lambda function to filter names in the RDD so that it only retains those starting with the letter 'M'

from pyspark.sql import SparkSession

# Initialize SparkSession to perform filter operations
spark = SparkSession.builder \
    .master("local") \
    .appName("FilterTransformation") \
    .getOrCreate()

# Create an RDD of names
rdd = spark.sparkContext.parallelize(["Michael", "Sarah", "Jessica", "Matthew", "Laura"])

# TODO: Change the lambda function to filter only names starting with 'M'
m_names_rdd = rdd.filter(lambda name: name.startswith('M'))

# Retrieve and print the filtered elements from the RDD
print("Names starting with 'M':", m_names_rdd.collect())

# Stop SparkSession to release resources
spark.stop()