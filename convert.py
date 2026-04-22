import pandas as pd

print("Loading CSV...")
df = pd.read_csv('contributions.csv', low_memory=False)

# Clean the amount column so it is natively a number in the Parquet file!
print("Cleaning data...")
df['amount'] = df['amount'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False)
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

# Save to Parquet
print("Saving to Parquet...")
df.to_parquet('contributions.parquet', index=False)
print("Done! You can now use contributions.parquet")