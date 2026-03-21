# complete the initialization and training of a logistic regression model

from pyspark.sql import SparkSession
from preprocess_data import preprocess_data
from pyspark.ml.classification import LogisticRegression

# Initialize a Spark session
spark = SparkSession.builder.appName("ModelTraining").getOrCreate()

# Preprocess the dataset
train_data, test_data = preprocess_data(spark, "iris.csv")

# TODO: Initialize the logistic regression model with specified feature and label columns
lr = LogisticRegression(featuresCol="features", labelCol="label")

# TODO: Fit the logistic regression model to the training data
lr_model = lr.fit(train_data)

# Display model parameters
print("Coefficient Matrix:\n", lr_model.coefficientMatrix)
print("Intercept Vector:", lr_model.interceptVector)

# Stop the Spark session
spark.stop()