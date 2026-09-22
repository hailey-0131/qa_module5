import pandas as pd

books = pd.read_csv("library.csv")
print(books.head())
customers = pd.read_csv("library_customers.csv")
print(customers.head())

print(books.shape)
print(books.columns.tolist()) # print column names
quant = len(books.to_string().splitlines())
print(quant)
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

output = books.loc[books.isnull().all(axis=1)].to_string()
print(output)

# when we don't let default fail/decide silently -> you decide the rows fate yourself
# the difference being in the early coerce examples, we handed control to the func, it promoted what it could
# the rest was removed

dropped_na = books.dropna()  # little less harsh than any, e.g. row that is missing a single field
dropped_na.shape  # gives me the updated dimension
dropped_na.isna().sum()  # count for present na values, has it worked?
books.isna().sum()  # compare with the above for missing value removeal
# books["loan amount.."].mean()

filled_value = books.fillna("value")  # inplace errors, see value handed back to the col with a new type
## this went from dtype float to text ^ value
filled_value.isnull().sum().sum()  # 0
# filled_value["Customer"].tolist()[-1]  # value


### duplications
print(books.duplicated().sum())
print(books.drop_duplicates().shape)
print(dropped_na.duplicated().sum())
