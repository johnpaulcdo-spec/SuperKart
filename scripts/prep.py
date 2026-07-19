import os
import pandas as pd
from datasets import Dataset

# Load your raw data
df = pd.read_csv("data/SuperKart.csv")

# Basic cleaning
df = df.dropna()

# Convert to Hugging Face Dataset
dataset = Dataset.from_pandas(df)

# Push to Hugging Face Hub (uses HF_TOKEN from the workflow environment)
dataset.push_to_hub(
    "johnpaulcdo-spec/superkart-dataset",
    token=os.environ["HF_TOKEN"],
)
print("✅ Data preparation complete and uploaded.")
