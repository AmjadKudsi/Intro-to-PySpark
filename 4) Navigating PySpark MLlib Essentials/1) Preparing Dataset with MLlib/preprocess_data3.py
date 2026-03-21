# identify and fix the issue, ensuring smooth data preprocessing operations

from pyspark.ml.feature import StringIndexer, VectorAssembler

def preprocess_data(spark, data_path):
    # Load the dataset
    raw_data = spark.read.csv(data_path, header=True, inferSchema=True)

    # Use 'species' column as the input for StringIndexer
    indexer = StringIndexer(inputCol="species", outputCol="label")
    
    # Transform the data to include the 'label' column with indexed values
    indexed_data = indexer.fit(raw_data).transform(raw_data)

    # Specify feature columns to be combined into a single 'features' vector
    assembler = VectorAssembler(
        inputCols=["sepal_length", "sepal_width", "petal_length", "petal_width"],
        outputCol="features"
    )

    # Transform the data to include the new 'features' column with vectorized features
    vectorized_data = assembler.transform(indexed_data)
    
    # Select only the 'features' and 'label' columns
    final_data = vectorized_data.select("features", "label")

    # Split the data into training and test sets
    train_data, test_data = final_data.randomSplit([0.8, 0.2], seed=42)

    return train_data, test_data