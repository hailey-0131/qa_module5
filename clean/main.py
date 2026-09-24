# importing funtions
from library_clean import (
    load_data,
    clean_books,
    clean_customers,
    save_data
)

def main():
    print("Starting library data cleaning...")
    books, customers = load_data()
    cleaned_books = clean_books(books)
    cleaned_customers = clean_customers(customers)
    save_data(cleaned_books, cleaned_customers)
    print("Data cleaning completed successfully.")

if __name__ == "__main__":
    main()
