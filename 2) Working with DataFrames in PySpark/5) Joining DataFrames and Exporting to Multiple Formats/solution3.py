# complete some missing code sections that address DataFrame operations in PySpark

from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("JoiningAndSavingDataFrames").getOrCreate()

# Read the CSV files into DataFrames
dept_df = spark.read.csv("departments.csv", header=True, inferSchema=True)
emp_df = spark.read.csv("employees.csv", header=True, inferSchema=True)

# TODO: Perform an inner join on the DeptID column
inner_joined_df = dept_df.join(emp_df, "DeptID")

# TODO: Display the DataFrame resulting from the inner join
inner_joined_df.show()

# TODO: Save the inner joined DataFrame as a CSV file at the path "output/inner_joined_data"
inner_joined_df.write.csv("output/inner_joined_data", header=True)

# Stop the SparkSession to release resources
spark.stop()