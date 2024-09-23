
import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Parameters for synthetic data generation
num_records = 1000  # Number of synthetic records to generate

# Function to generate synthetic data
def generate_synthetic_data(num_records):
    data = {
        'customer_id': [fake.unique.random_int(min=10000, max=99999) for _ in range(num_records)],
        'transaction_amount': np.random.normal(1000, 500, num_records).round(2),  # Mean=1000, Std=500
        'credit_score': np.random.randint(300, 850, num_records),  # Typical credit scores range
        'income': np.random.normal(50000, 15000, num_records).round(2),  # Mean=50k, Std=15k
        'employment_status': np.random.choice(['Full-time', 'Part-time', 'Self-employed', 'Unemployed'], num_records),
        'default_status': np.random.choice([0, 1], num_records, p=[0.9, 0.1])  # 90% no default, 10% default
    }
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    return df

# Generate data
synthetic_data = generate_synthetic_data(num_records)

# Save to CSV
csv_file_path = 'data/credit_risk_data.csv'  # Path to save the synthetic data
synthetic_data.to_csv(csv_file_path, index=False)
print(f"Synthetic data generated and saved to {csv_file_path}")
