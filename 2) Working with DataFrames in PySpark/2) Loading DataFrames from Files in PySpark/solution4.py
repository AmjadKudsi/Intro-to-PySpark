# data is structured in an array (means all the data entries are grouped within square brackets [])
# set the multiLine option to True

from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("LoadingDataFrames").getOrCreate()

# TODO: Change the JSON loading method to read from a file structured as an array
json_df = spark.read.json("data_array.json", multiLine=True)

# Display the first 3 rows of the JSON DataFrame
json_df.show(3)

# Stop the SparkSession to release resources
spark.stop()