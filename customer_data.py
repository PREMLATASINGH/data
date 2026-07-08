import pandas as pd
import numpy as np
import random

# Sample data pools
names = [
    "Amit Sharma", "Priya Verma", "John Doe", "Sara Khan", "Ravi Patel",
    "Neha Singh", "Arjun Mehta", "Emily Clark", "David Miller", "Sonia Kapoor",
    "Rahul Nair", "Kavita Joshi", "Michael Brown", "Sophia Wilson", "Vikram Rao",
    "Anita Desai", "Chris Evans", "Nisha Reddy", "Kabir Malhotra", "Olivia Taylor"
]

cities = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai",
    "New York", "Chicago", "San Francisco", "Houston", "Boston"
]

# Generate 200 rows
num_rows = 200
data = {
    "CustomerID": np.arange(1001, 1001 + num_rows),
    "Name": [random.choice(names) for _ in range(num_rows)],
    "Age": np.random.randint(18, 65, num_rows),
    "City": [random.choice(cities) for _ in range(num_rows)],
    "PurchaseAmount": np.round(np.random.uniform(50, 1000, num_rows), 2)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("customer_200.csv", index=False)

print("customer_200.csv created successfully!")
