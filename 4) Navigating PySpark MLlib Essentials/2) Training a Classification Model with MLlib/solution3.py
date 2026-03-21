# complete the code to ensure the logistic regression model functions correctly

from pyspark.sql import SparkSession
from preprocess_data import preprocess_data
from pyspark.ml.classification import LogisticRegression

# Initialize a Spark session
spark = SparkSession.builder.appName("ModelTraining").getOrCreate()

# Preprocess the dataset
train_data, test_data = preprocess_data(spark, "iris.csv")

# TODO: Initialize the LogisticRegression model with the appropriate feature and label columns
lr = LogisticRegression(featuresCol="features", labelCol="label")

# TODO: Fit the logistic regression model to the training data and store the model
lr_model = lr.fit(train_data)

# TODO: Display the coefficientMatrix from the trained model
print("Coefficient Matrix:\n", lr_model.coefficientMatrix)

# TODO: Display the interceptVector from the trained model
print("Intercept Vector:\n", lr_model.interceptVector)

# Stop the Spark session
spark.stop()