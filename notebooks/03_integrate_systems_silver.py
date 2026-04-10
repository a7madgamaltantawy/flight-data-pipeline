from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("IntegrateSystemsSilver").getOrCreate()

# Paths
validated_flight_path = "abfss://processed@<storage_account>.dfs.core.windows.net/silver/validated_flight_data"
battery_input_path = "abfss://raw-data@<storage_account>.dfs.core.windows.net/battery_data.csv"
control_input_path = "abfss://raw-data@<storage_account>.dfs.core.windows.net/control_system.csv"
silver_output_path = "abfss://processed@<storage_account>.dfs.core.windows.net/silver/integrated_telemetry_data"

# Read datasets
df_flight = spark.read.parquet(validated_flight_path)
df_battery = spark.read.csv(battery_input_path, header=True, inferSchema=True)
df_control = spark.read.csv(control_input_path, header=True, inferSchema=True)

# Integrate subsystems on flight_id and timestamp
df_integrated = (
    df_flight
    .join(df_battery, ["flight_id", "timestamp"], "inner")
    .join(df_control, ["flight_id", "timestamp"], "inner")
)

# Save integrated silver layer
df_integrated.write.mode("overwrite").parquet(silver_output_path)

print("System integration completed successfully.")
print(f"Integrated rows: {df_integrated.count()}")
