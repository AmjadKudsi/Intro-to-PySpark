# modify the code to left join and save the resulting DataFrame as a JSON file

from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.master("local").appName("JoiningAndSavingDataFrames").getOrCreate()

# Read the CSV files into DataFrames
dept_df = spark.read.csv("departments.csv", header=True, inferSchema=True)
emp_df = spark.read.csv("employees.csv", header=True, inferSchema=True)

# TODO: Perform a left join on the DeptID column
joined_df = dept_df.join(emp_df, "DeptID", "left")

# Display the DataFrame resulting from the join
joined_df.show()

# TODO: Save the DataFrame as a JSON file
joined_df.write.json("output/joined_data")

# Stop the SparkSession to release resources
spark.stop()