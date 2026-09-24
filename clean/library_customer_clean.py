import pandas as pd
customers = pd.read_csv("library_customers.csv")
print(customers)

# Remove rows with NA
def remove_na(df): 
    return df.dropna()

# Convert column types
def convert_col(df):
    # Convert ID column to integer
    df["Customer ID"] = df["Customer ID"].astype("int64")
    return df

def clean_data(df):
    df = remove_na(df)
    df = convert_col(df)
    return df

print(clean_data(customers))
