# identify and correct multiple mistakes in the provided code so that the logistic regression model properly trains on the data

from pyspark.sql import SparkSession
from preprocess_data import preprocess_data
from pyspark.ml.classification import LogisticRegression

# Initialize a Spark session
spark = SparkSession.builder.appName("ModelTraining").getOrCreate()

# Preprocess the dataset
train_data, test_data = preprocess_data(spark, "iris.csv")

# Initialize the logistic regression model with specified feature and label columns
lr = LogisticRegression(featuresCol="features", labelCol="label")

# Fit the logistic regression model to the training data
lr_model = lr.fit(train_data)

# Display model parameters
print("Coefficient Matrix:\n", lr_model.coefficientMatrix)
print("Intercept Vector:", lr_model.interceptVector)

# Stop the Spark session
spark.stop()