from datasets import load_dataset
import pandas as pd

dataset = load_dataset("afrias5/FinalTestFeed4096AllCriteriaResponse")

data = dataset["train"] 

df = pd.DataFrame(data)

output_csv = "FinalTestFeed4096AllCriteriaResponse.csv"
df.to_csv(output_csv, index=False)

print(f"Saved dataset to: {output_csv}")
