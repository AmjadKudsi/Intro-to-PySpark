# retain only log lines that include the keyword "INFO"

from pyspark.sql import SparkSession

# Initialize SparkSession to perform filter operations
spark = SparkSession.builder \
    .master("local") \
    .appName("FilterTransformation") \
    .getOrCreate()

# Read the text file into an RDD
rdd = spark.sparkContext.textFile("logs.txt")

# TODO: Filter the RDD to retain only log lines containing the keyword "INFO" using a lambda function
rdd_filter = rdd.filter(lambda x: "INFO" in x)


# TODO: Retrieve and print the filtered elements from the RDD
print("Filtered elements: ", rdd_filter.collect())


# Stop SparkSession to release resources
spark.stop()