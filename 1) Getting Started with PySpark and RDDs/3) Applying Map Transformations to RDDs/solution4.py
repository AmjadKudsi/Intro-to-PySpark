# replace underscores with dashes

from pyspark.sql import SparkSession

# Initialize SparkSession for transformation operations
spark = SparkSession.builder \
    .master("local") \
    .appName("MapTransformation") \
    .getOrCreate()

# Create an RDD with username strings containing underscores
rdd = spark.sparkContext.parallelize(["john_doe", "jane_smith", "alice_wonderland", "bob_builder", "charlie_brown"])

# TODO: Apply a map transformation to replace underscores with dashes in each username
rdd_dashes = rdd.map(lambda name: name.replace('_','-'))


# TODO: Retrieve and print the transformed usernames from the RDD
print("Transformed usernames: ", rdd_dashes.collect())


# Stop SparkSession to release resources
spark.stop()