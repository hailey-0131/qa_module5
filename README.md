# Library Data Quality Project

## Project Overview

This project was created to improve the quality and reliability of library datasets using Python.

The original data contained a number of data-quality issues, including:

- Invalid or incorrectly formatted dates
- Duplicate records
- Extra spaces in text fields
- Books having returned before their checkout date
- Books being returned more than 14 days after checkout
- Library records that could not be matched to a customer

The project uses Python and pandas to clean, validate and transform the data before producing cleaned CSV files that can be used for reporting and analysis.

---

## Project Objectives

The main objectives of the project are to:

- Automate repetitive data-cleaning tasks
- Identify and flag data-quality problems
- Standardise data into consistent formats
- Produce clean datasets ready for analysis
- Test the cleaning functions using automated unit tests
- Automatically run the project when changes are pushed to GitHub
- Package and run the application using Docker

---

## Project Structure

```text
library-data-quality/
│
├── data/
│   └── source CSV files
│
├── main.yml
├── main.py
│   └── library_clean.py
│       └── load_data
│       └── clean_books
│       └── clean_customers
│       └── save_data
│   └── library_clean_test.py
│
├── docker/
│   └── Dockerfile
│
└── output/
    ├── library_cleaned.csv
    └── library_customers_cleaned.csv
