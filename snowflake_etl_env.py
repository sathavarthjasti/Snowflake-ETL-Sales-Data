import pandas as pd
import snowflake.connector
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")
SNOWFLAKE_TABLE = "SALES_DATA"
CSV_FILE_PATH = "sales_data.csv"

#To Verify Env Configuration Check
print("Config Check:")
print("Account:", SNOWFLAKE_ACCOUNT)
print("User:", SNOWFLAKE_USER)
print("Password:", "SAFE" if SNOWFLAKE_PASSWORD else "MISSING")
print("Warehouse:", SNOWFLAKE_WAREHOUSE)
print("Database:", SNOWFLAKE_DATABASE)
print("Schema:", SNOWFLAKE_SCHEMA)

# Simulate Raw Sales Data
data = {
    "date": pd.date_range(start="2021-01-01", periods=10).astype(str),
    "region": ["East", "West", "North", "South", "East", "West", "North", "South", "East", "West"],
    "product": ["Widget", "Gadget", "Widget", "Gadget", "Widget", "Gadget", "Widget", "Gadget", "Widget", "Gadget"],
    "units_sold": [10, 15, 5, 12, 7, 18, 6, 11, 9, 14],
    "unit_price": [20.0, 25.0, 20.0, 25.0, 20.0, 25.0, 20.0, 25.0, 20.0, 25.0]
}
df = pd.DataFrame(data)
df["total_revenue"] = df["units_sold"] * df["unit_price"]
df.to_csv(CSV_FILE_PATH, index=False)

# Load to Snowflake
try:
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA
    )
    cursor = conn.cursor()

    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {SNOWFLAKE_SCHEMA}.{SNOWFLAKE_TABLE} (
            date DATE,
            region STRING,
            product STRING,
            units_sold INTEGER,
            unit_price FLOAT,
            total_revenue FLOAT
        );
    """)

    for _, row in df.iterrows():
        cursor.execute(
            f"""
            INSERT INTO {SNOWFLAKE_SCHEMA}.{SNOWFLAKE_TABLE} (date, region, product, units_sold, unit_price, total_revenue)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, tuple(row)
        )

    print("Sales data loaded successfully into Snowflake.")
except Exception as e:
    print(f"Failed to load data into Snowflake: {e}")
finally:
    try:
        cursor.close()
        conn.close()
    except:
        pass
