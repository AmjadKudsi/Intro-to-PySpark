# complete the code

from pyspark.sql import SparkSession
from preprocess_data import preprocess_data
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Initialize a Spark session
spark = SparkSession.builder.appName("ModelEvaluation").getOrCreate()

# Preprocess the dataset
train_data, test_data = preprocess_data(spark, "iris.csv")

# Initialize the logistic regression model with specified feature and label columns
lr = LogisticRegression(featuresCol="features", labelCol="label")

# Fit the logistic regression model to the training data
lr_model = lr.fit(train_data)

# TODO: Make predictions on the test set
predictions = lr_model.transform(test_data)

# TODO: Initialize a MulticlassClassificationEvaluator to calculate accuracy
evaluator = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="accuracy"
)

# TODO: Compute the accuracy of the model on the test data
accuracy = evaluator.evaluate(predictions)

# TODO: Display the calculated accuracy of the model
print("Model Accuracy:", accuracy)

# Stop the Spark session
spark.stop()