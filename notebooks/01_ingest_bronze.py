from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("IngestBronze").getOrCreate()

# Paths
flight_input_path = "abfss://raw-data@<storage_account>.dfs.core.windows.net/flight_data.csv"
battery_input_path = "abfss://raw-data@<storage_account>.dfs.core.windows.net/battery_data.csv"
control_input_path = "abfss://raw-data@<storage_account>.dfs.core.windows.net/control_system.csv"

bronze_flight_output = "abfss://processed@<storage_account>.dfs.core.windows.net/bronze/flight_data"
bronze_battery_output = "abfss://processed@<storage_account>.dfs.core.windows.net/bronze/battery_data"
bronze_control_output = "abfss://processed@<storage_account>.dfs.core.windows.net/bronze/control_system"

# Read CSVs
df_flight = spark.read.csv(flight_input_path, header=True, inferSchema=True)
df_battery = spark.read.csv(battery_input_path, header=True, inferSchema=True)
df_control = spark.read.csv(control_input_path, header=True, inferSchema=True)

# Save as bronze parquet
df_flight.write.mode("overwrite").parquet(bronze_flight_output)
df_battery.write.mode("overwrite").parquet(bronze_battery_output)
df_control.write.mode("overwrite").parquet(bronze_control_output)

print("Bronze ingestion completed successfully.")
