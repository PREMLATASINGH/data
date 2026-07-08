import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Sample pools
products = [
    "Laptop", "Mobile Phone", "Headphones", "Keyboard", "Mouse",
    "Smartwatch", "Tablet", "Monitor", "USB Drive", "Printer"
]

# Customer IDs (you can match these with your customer table)
customer_ids = np.arange(1001, 1011)  # 10 customers: 1001–1010

# Generate random dates (last 60 days)
def random_date():
    start = datetime.now() - timedelta(days=60)
    random_days = random.randint(0, 60)
    return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")

# Number of rows
num_rows = 20

data = {
    "OrderID": np.arange(5001, 5001 + num_rows),
    "CustomerID": [random.choice(customer_ids) for _ in range(num_rows)],
    "Product": [random.choice(products) for _ in range(num_rows)],
    "Quantity": np.random.randint(1, 5, num_rows),
    "Price": np.round(np.random.uniform(20, 1500, num_rows), 2),
    "OrderDate": [random_date() for _ in range(num_rows)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save CSV
df.to_csv("orders_20_with_customerid.csv", index=False)

print("orders_20_with_customerid.csv created successfully!")

