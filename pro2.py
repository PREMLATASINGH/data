import pandas as pd
import numpy as np
import random

# Number of rows
n = 500

# Sample data pools
first_names = ["Aarav", "Vivaan", "Aditya", "Kabir", "Rohan", "Ishaan", "Kavya", "Diya", "Ananya", "Riya"]
last_names = ["Sharma", "Verma", "Patel", "Reddy", "Singh", "Gupta", "Nair", "Iyer", "Das", "Khan"]
cities = ["Edison", "New Brunswick", "Jersey City", "Princeton", "Woodbridge", "Iselin"]
grades = ["A", "B", "C", "D"]
years = list(range(2018, 2026))

# Helper to generate phone numbers
def generate_phone():
    return f"732-{random.randint(200,999)}-{random.randint(1000,9999)}"

# Generate dataset
data = {
    "student_id": np.arange(1, n+1),
    "full_name": [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(n)],
    "age": np.random.randint(15, 22, n),
    "city": [random.choice(cities) for _ in range(n)],
    "grade": [random.choice(grades) for _ in range(n)],
    "math_marks": np.random.randint(40, 100, n),
    "science_marks": np.random.randint(40, 100, n),
    "english_marks": np.random.randint(40, 100, n),
    "enrollment_year": [random.choice(years) for _ in range(n)],
    "email": [],
    "phone": [generate_phone() for _ in range(n)]
}

# Generate emails based on names
for name in data["full_name"]:
    email = name.lower().replace(" ", ".") + "@school.edu"
    data["email"].append(email)
    


# Create DataFrame
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)


print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.isnull().sum())
print(df['grade'].value_counts())
print(df['city'].value_counts())
print(df.groupby('enrollment_year')['student_id'].count())
print(df.groupby('grade')['math_marks'].mean())
print(df.groupby('grade')['science_marks'].mean())
print(df.groupby('grade')['english_marks'].mean())
print(df.sort_values(by='math_marks', ascending=False).head(10))
print(df.sort_values(by='science_marks', ascending=False).head(10))
print(df.sort_values(by='english_marks', ascending=False).head(10))
print(df[df['math_marks'] < 50])
print(df[df['science_marks'] < 50])
print(df[df['english_marks'] < 50])
print(df[df['math_marks'] >= 80])
print(df[df['science_marks'] >= 80])
print(df[df['english_marks'] >= 80])
print(df[df['age'] < 18])
print(df[df['age'] >= 18])
print(df[df['city'] == 'Edison'])
print(df[df['city'] == 'New Brunswick'])
print(df.columns)
print(df.dtypes)
print(df.nunique())
print(df.index)
print(df['city'].unique())
print(df['grade'].unique())