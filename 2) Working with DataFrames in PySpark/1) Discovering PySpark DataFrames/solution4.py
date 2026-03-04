# complete the code

from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("BasicOperations").getOrCreate()

# Create a simple list of tuples representing data
data = [("Alice", 1), ("Bob", 2), ("Cathy", 1)]

# TODO: Create a DataFrame directly from the list
# - Use "Name" and "Value" as column names
df_from_list = spark.createDataFrame(data, ["Name", "Value"])

# TODO: Show the contents of the DataFrame created from the list
df_from_list.show(0)

# TODO: Print the schema of the DataFrame created from the list
df_from_list.printSchema()

# Convert the list into an RDD
rdd = spark.sparkContext.parallelize(data)

# TODO: Create a DataFrame from the existing RDD
# - Use "Name" and "Value" as column names
df_from_rdd = spark.createDataFrame(rdd,["Name", "Value"])

# TODO: Print the number of rows in the DataFrame created from the RDD
print("Number of rows in the DataFrame: ", df_from_rdd.count())

# Stop the SparkSession to release resources
spark.stop()