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
├── .github/
│   └── workflows/                  # GitHub Actions workflows
│       └── main.yml                # CI/CD workflow
│
├── clean/                          # Python cleaning code and tests
│   ├── main.py                     # Runs the data cleaning process
│   ├── library_clean.py            # Data cleaning functions
│   └── library_clean_test.py       # Unit tests
│
├── data/                           # Source CSV files
│   └── source CSV files
│
├── docker/                         # Docker configuration
│   └── Dockerfile
│
├── .gitignore                      # Files/folders excluded from Git
├── README.md                       # Project documentation
└── requirements.txt                # Required Python packages
