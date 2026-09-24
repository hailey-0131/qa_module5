# Library Data Quality Project

## [Loan Analysis Dashboard](https://app.powerbi.com/groups/me/reports/c49a9943-22ec-46b3-9ef0-f99eb5bacea5?ctid=e7a5c1ab-1c72-45e2-bc54-8984092104fa&pbi_source=linkShare)

A Power BI dashboard was developed using the cleaned library data to provide an overview of loan activity and highlight potential data-quality issues.

The dashboard contains two main pages:

### Loan Analysis

Provides an overview of library loan activity, including:

- Total number of loans
- Number and percentage of late returns
- Analysis of loan and return activity
- Key trends and patterns within the cleaned data

### Data Quality

Provides visibility of records where data-quality issues were identified during the Python cleaning process.

This page allows users to:

- View records that have been flagged with a data-quality issue
- Identify the type of issue affecting each record


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

## Repository Structure

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
