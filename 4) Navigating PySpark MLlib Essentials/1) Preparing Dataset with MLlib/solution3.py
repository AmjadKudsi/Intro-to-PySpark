# identify and fix the issue, ensuring smooth data preprocessing operations

from pyspark.sql import SparkSession
from preprocess_data import preprocess_data

# Initialize a Spark session
spark = SparkSession.builder.appName("PreprocessData").getOrCreate()

# Preprocess the dataset
train_data, test_data = preprocess_data(spark, "iris.csv")

# Show the first rows in the training data
print("First Training Data Rows:")
train_data.show()

# Show the first rows in the test data
print("First Test Data Rows:")
test_data.show()

# Stop the Spark session
spark.stop()