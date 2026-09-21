import pandas as pd

books = pd.read_csv("library.csv")
print(books.head())
customers = pd.read_csv("library_customers.csv")
print(customers.head())

print(books.shape)
count = books.isnull().all().sum()
real = books.dropna(how="any")
print(real.shape)
print(real)

books['Id']
three_books = books['Id'].head(3).tolist()
print(books.dtypes)

silence_error = pd.to_datetime(books['Book checkout'], dayfirst=True, errors='coerce')
print(silence_error.dtype)
print(books.duplicated())
