# complete the code

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

# TODO: Perform a left join on the DeptID column
left_joined_df = dept_df.join(emp_df, "DeptID", "left")

# TODO: Display the DataFrame resulting from the left join
left_joined_df.show()

# TODO: Perform a right join on the DeptID column
right_joined_df = dept_df.join(emp_df, "DeptID", "right")

# TODO: Display the DataFrame resulting from the right join
right_joined_df.show()

# TODO: Save the inner joined DataFrame as a CSV file "output/inner_joined_data"
inner_joined_df.write.csv("output/inner_joined_data", header=True)

# TODO: Save the left joined DataFrame as a JSON file "output/left_joined_data"
left_joined_df.write.json("output/left_joined_data")

# TODO: Save the right joined DataFrame as a Parquet file at "output/right_joined_data"
right_joined_df.write.parquet("output/right_joined_df")

# Stop the SparkSession to release resources
spark.stop()