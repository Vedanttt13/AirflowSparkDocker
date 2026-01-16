from pyspark.sql import SparkSession

def main():
    # Create Spark Session
    spark = SparkSession.builder \
        .appName("Sample Spark Job") \
        .getOrCreate()
    
    # Sample data
    data = [
        ("Alice", 25, "Engineer"),
        ("Bob", 30, "Data Scientist"),
        ("Charlie", 35, "Manager"),
        ("David", 28, "Developer"),
        ("Eve", 32, "Analyst")
    ]
    
    # Create DataFrame
    columns = ["Name", "Age", "Job"]
    df = spark.createDataFrame(data, columns)
    
    # Show DataFrame
    print("Original DataFrame:")
    df.show()
    
    # Filter data
    filtered_df = df.filter(df.Age > 28)
    print("\nFiltered DataFrame (Age > 28):")
    filtered_df.show()
    
    # Group by Job
    job_count = df.groupBy("Job").count()
    print("\nJob Count:")
    job_count.show()
    
    # Stop Spark Session
    spark.stop()
    print("Spark job completed successfully!")

if __name__ == "__main__":
    main()
