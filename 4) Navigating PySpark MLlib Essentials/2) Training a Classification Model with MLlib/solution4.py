# switch from using a logistic regression model to a decision tree classifier within PySpark's MLlib

from pyspark.sql import SparkSession
from preprocess_data import preprocess_data
# TODO: Import the DecisionTreeClassifier instead of LogisticRegression
from pyspark.ml.classification import DecisionTreeClassifier

# Initialize a Spark session
spark = SparkSession.builder.appName("ModelTraining").getOrCreate()

# Preprocess the dataset
train_data, test_data = preprocess_data(spark, "iris.csv")

# TODO: Change the model
# - Replace LogisticRegression with DecisionTreeClassifier
# - Update the variable name to indicate the model type (e.g., `lr` to `dt`)
dt = DecisionTreeClassifier(featuresCol="features", labelCol="label")

# TODO: Fit the DecisionTreeClassifier instance to the training data
model = dt.fit(train_data)

# TODO: Print depth of the decision tree, use model.depth
print("Coefficient Matrix:\n", model.depth)

# TODO: Print number of leaves in the decision tree, use model.numNodes
print("Intercept Vector:", model.numNodes)

# Stop the Spark session
spark.stop()