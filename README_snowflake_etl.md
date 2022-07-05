# ❄️ Snowflake Sales ETL Project

This project demonstrates how to build an end-to-end **ETL pipeline** using **Python** and **Snowflake**, capable of simulating sales data, transforming it using `pandas`, and loading it into a Snowflake table.

---

## 📦 Features

- ✅ Simulates structured sales data
- 🔄 Transforms data to calculate total revenue
- ⛓️ Connects to Snowflake via secure credentials
- 📤 Creates a table if it doesn't exist
- 📈 Loads data row-by-row into the Snowflake `SALES_DATA` table

---

## ⚙️ Tech Stack

- **Python 3.8+**
- `pandas` for data manipulation
- `snowflake-connector-python` for database connectivity
- `dotenv` for secure credential loading

---

## 🧪 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/snowflake-etl-project.git
cd snowflake-etl-project
```

### 2️⃣ Create a `.env` file
In the root directory, add your Snowflake credentials to a `.env` file:

```env
SNOWFLAKE_ACCOUNT=xy12345.us-east-1
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
SNOWFLAKE_DATABASE=DEMO_DB
SNOWFLAKE_SCHEMA=PUBLIC
```

> ⚠️ **Do not commit** the `.env` file to version control.

### 3️⃣ Install dependencies
```bash
pip install pandas snowflake-connector-python python-dotenv
```

### 4️⃣ Run the ETL script
```bash
python snowflake_etl_env.py
```

---

## 📊 Output

After successful execution, a `SALES_DATA` table will be created in your Snowflake database containing:

| date       | region | product | units_sold | unit_price | total_revenue |
|------------|--------|---------|------------|-------------|----------------|
| 2021-01-01 | East   | Widget  | 10         | 20.0        | 200.0          |
| ...        | ...    | ...     | ...        | ...         | ...            |

---


## 📝 License

This project is open-sourced under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Built by [@sathavarthjasti](https://github.com/sathavarthjasti) 