from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("ValidateFlightData").getOrCreate()

# Paths
flight_input_path = "abfss://raw-data@<storage_account>.dfs.core.windows.net/flight_data.csv"
validated_output_path = "abfss://processed@<storage_account>.dfs.core.windows.net/silver/validated_flight_data"

# Read raw flight data
df_flight = spark.read.csv(
    flight_input_path,
    header=True,
    inferSchema=True
)

# Basic validation rules
df_validated = df_flight.filter(
    (col("altitude") > 0) &
    (col("speed") > 0) &
    (col("temperature").isNotNull())
)

# Save validated flight data
df_validated.write.mode("overwrite").parquet(validated_output_path)

print("Flight validation completed successfully.")
print(f"Validated rows: {df_validated.count()}")
