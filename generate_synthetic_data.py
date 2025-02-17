import pandas as pd
from faker import Faker
import random

# Initialize Faker to generate fake customer inquiries
fake = Faker()

# Define sample customer support categories
categories = [
    "Billing Issue",
    "Technical Support",
    "Account Management",
    "General Inquiry",
    "Product Information",
    "Cancellation Request",
    "Refund Request",
    "Shipping Inquiry"
]

# Generate synthetic customer support queries
num_samples = 1000  # Adjust as needed
data = []

for _ in range(num_samples):
    issue_type = random.choice(categories)
    
    if issue_type == "Billing Issue":
        text = f"My bill amount is incorrect. Can you check my latest invoice?"
    elif issue_type == "Technical Support":
        text = f"I am unable to log into my account. It keeps showing an error."
    elif issue_type == "Account Management":
        text = f"How do I update my email and password for my account?"
    elif issue_type == "General Inquiry":
        text = f"Can you tell me about the features of your premium plan?"
    elif issue_type == "Product Information":
        text = f"Is the new version of your product available in my region?"
    elif issue_type == "Cancellation Request":
        text = f"I want to cancel my subscription. How do I proceed?"
    elif issue_type == "Refund Request":
        text = f"I was charged incorrectly and need a refund. What should I do?"
    elif issue_type == "Shipping Inquiry":
        text = f"When will my order be delivered? Can I track my shipment?"
    
    data.append([text, issue_type])

# Create a DataFrame
df = pd.DataFrame(data, columns=["customer_query", "category"])

# Save to CSV
csv_filename = "customer_support_data.csv"
df.to_csv(csv_filename, index=False)

print(f"Synthetic customer support data saved as {csv_filename}")
