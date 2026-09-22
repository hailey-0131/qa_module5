import pandas as pd
books = pd.read_csv("library.csv")

# ---------------- CLEANING FUNCTIONS ----------------

# Remove rows with NA
def remove_na(df): 
    return df.dropna()

# Remove duplicate rows
# Remove duplicate rows, but ignore the ID column
def remove_dupes(df):
    # Get all columns except ID
    cols = [col for col in df.columns if col != "Id"]
    # Check for duplicates using those columns only
    return df.drop_duplicates(subset=cols)

# Clean text
def strip_text(df):
    for col in df.columns:
        if pd.api.types.is_string_dtype(df[col]):
            df[col] = df[col].str.strip()
    return df

# Convert column types
def convert_col(df):
    # Convert ID columns to integer
    df["Id"] = df["Id"].astype("int64")
    df["Customer ID"] = df["Customer ID"].astype("int64")
    # Convert date columns to date
    cleaned_checkout = df["Book checkout"].str.strip().str.strip('"')
    df["Book checkout"] = pd.to_datetime(cleaned_checkout, errors="coerce", dayfirst=True)
    df["Book Returned"] = pd.to_datetime(df["Book Returned"], errors="coerce", dayfirst=True)
    return df

# Calculate days to borrow
def calc_days(df):
    def convert(data):        
        # Split the value into the number and unit
        number, unit = data.split()
        # Convert the number from text to an integer
        number = int(number)
        # Convert weeks to days
        if "week" in unit.lower():
            return number * 7
        # Convert months to days
        elif "month" in unit.lower():
            return number * 30
        # If the value is already in days
        elif "day" in unit.lower():
            return number
        else:
            raise ValueError(f"Unrecognised time unit")
    df["Days allowed to borrow"] = df["Days allowed to borrow"].apply(convert)
    return df


# ---------------- CALL ALL CLEANING FUNCTIONS ----------------
def clean_data(df):
    df = remove_na(df)
    df = remove_dupes(df)
    df = strip_text(df)
    df = convert_col(df)
    df = calc_days(df)
    return df

# Check if dates make sense
def check_data_quality(df):
    def check_row(row):
        if row["Book checkout"] > row["Book Returned"]:
            return "Checkout date after returned date"
        elif pd.isna(row["Book checkout"]):
            return "Invalid checkout date"
        elif pd.isna(row["Book Returned"]):
            return "Invalid returned date"
        else:
            return "Good"
    df["Data Quality"] = df.apply(check_row, axis=1)
    return df

# Check whether a book was returned more than 14 days after checkout
def check_late_return(df):
    # Calculate the number of days between checkout and return
    df["Days Borrowed"] = (df["Book Returned"] - df["Book checkout"]).dt.days
    # Check if the book was kept for more than 14 days
    df["Late Return"] = df["Days Borrowed"] > 14
    return df

# Results
# cleaned_data = clean_data(books)
# print(check_late_return(check_data_quality(cleaned_data)))