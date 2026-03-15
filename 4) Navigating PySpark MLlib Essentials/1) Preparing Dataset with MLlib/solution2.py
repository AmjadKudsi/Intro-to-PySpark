from pyspark.sql import SparkSession
from preprocess_data import preprocess_data

# Initialize a Spark session
spark = SparkSession.builder.appName("PreprocessData").getOrCreate()

# Preprocess the dataset
train_data, test_data = preprocess_data(spark, "iris.csv")

# Show the count of rows in the training data
print("Training Data Count:", train_data.count())

# Show the count of rows in the test data
print("Test Data Count:", test_data.count())

# Stop the Spark session
spark.stop()