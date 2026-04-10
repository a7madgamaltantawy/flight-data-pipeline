RAW_CONTAINER = "raw-data"
PROCESSED_CONTAINER = "processed"
STORAGE_ACCOUNT = "<storage_account>"

FLIGHT_DATA_PATH = f"abfss://{RAW_CONTAINER}@{STORAGE_ACCOUNT}.dfs.core.windows.net/flight_data.csv"
BATTERY_DATA_PATH = f"abfss://{RAW_CONTAINER}@{STORAGE_ACCOUNT}.dfs.core.windows.net/battery_data.csv"
CONTROL_DATA_PATH = f"abfss://{RAW_CONTAINER}@{STORAGE_ACCOUNT}.dfs.core.windows.net/control_system.csv"
