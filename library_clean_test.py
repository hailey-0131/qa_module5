import pandas as pd
import pytest


# Import the functions being tested from library_clean.py
from library_clean import (
    remove_na,
    remove_dupes,
    strip_text,
    convert_col,
    calc_days,
    clean_data,
    check_data_quality,
    check_late_return
)

@pytest.fixture
def df():
    books = pd.read_csv("library.csv")
    return books

# ---------------- TESTING FUNCTIONS ----------------
def test_remove_na():
    test_df = pd.DataFrame({
        "Id": [1, 2, 3],
        "Books": ["Dune", None, "IT"]
    })
    cleaned_df = remove_na(test_df)
    # ASSERT: no missing values should remain
    assert cleaned_df.isna().sum().sum() == 0
    # ASSERT: one row should have been removed
    assert len(cleaned_df) == 2

def test_remove_dupes():
    test_df = pd.DataFrame({
        "Id": [1, 2],
        "Books": ["Dune", "Dune"],
        "Customer ID": [101, 101]
    })
    cleaned_df = remove_dupes(test_df)
    # ASSERT: the two records should be treated as duplicates
    assert len(cleaned_df) == 1
    # ASSERT: the first record should be kept
    assert cleaned_df["Id"].iloc[0] == 1

def test_remove_dupes_keeps_different_records():
    test_df = pd.DataFrame({
        "Id": [1, 2],
        "Books": ["Dune", "IT"],
        "Customer ID": [101, 101]
    })
    cleaned_df = remove_dupes(test_df)
    # ASSERT: both records should remain
    assert len(cleaned_df) == 2

def test_strip_text():
    test_df = pd.DataFrame({
        "Books": [" Dune ", "IT  ", " The Hobbit"]
    })
    cleaned_df = strip_text(test_df)
    # ASSERT: no book titles should start with a space
    assert cleaned_df["Books"].str.startswith(" ").sum() == 0
    # ASSERT: no book titles should end with a space
    assert cleaned_df["Books"].str.endswith(" ").sum() == 0
    # ASSERT: values should match the expected results
    assert cleaned_df["Books"].tolist() == ["Dune","IT","The Hobbit"]

def test_convert_col_converts_ids_to_integers(df):
    test_df = pd.DataFrame({
        "Id": ["1", "2"],
        "Customer ID": ["101", "102"],
        "Book checkout": ['"20/02/2023"', '"20/05/2023"'],
        "Book Returned": ["25/02/2023", "25/08/2023"]
    })
    cleaned_df = convert_col(test_df)
    # ASSERT: both ID columns should be integer datatypes
    assert pd.api.types.is_integer_dtype(cleaned_df["Id"])
    assert pd.api.types.is_integer_dtype(cleaned_df["Customer ID"])

def test_convert_col_converts_dates():
    test_df = pd.DataFrame({
        "Id": ["1", "2"],
        "Customer ID": ["101", "102"],
        "Book checkout": ['"20/02/2023"', '"20/05/2023"'],
        "Book Returned": ["25/02/2023", "25/08/2023"]
    })
    cleaned_df = convert_col(test_df)
    # ASSERT: both columns should be datetime
    assert pd.api.types.is_datetime64_any_dtype(cleaned_df["Book checkout"])
    assert pd.api.types.is_datetime64_any_dtype(cleaned_df["Book Returned"])
    # ASSERT: the checkout value should be converted correctly
    assert cleaned_df["Book checkout"].iloc[0] == pd.Timestamp("2023-02-20")

def test_calc_days_invalid_unit_raises_error():
    test_df = pd.DataFrame({"Days allowed to borrow": ["2 years"]})
    # ACT and ASSERT: the function should raise an error
    with pytest.raises(ValueError):
        calc_days(test_df)

def test_checkout_after_return_is_flagged():
    test_df = pd.DataFrame({
        "Book checkout": [pd.Timestamp("2023-02-20")],
        "Book Returned": [pd.Timestamp("2023-02-10")]
    })
    checked_df = check_data_quality(test_df)
    # ASSERT: the date issue should be identified
    assert checked_df["Data Quality"].iloc[0] == ("Checkout date after returned date")


def test_clean_data(df):
    cleaned_df = clean_data(df)
    # Check that there are no rows where all columns are missing
    assert cleaned_df.isna().all(axis=1).sum() == 0
    # No trailing spaces in Books
    assert cleaned_df["Books"].str.endswith(" ").sum() == 0
    # ID is integer
    assert pd.api.types.is_integer_dtype(cleaned_df["Id"])
    # Checkout is a date
    assert pd.api.types.is_datetime64_any_dtype(cleaned_df["Book checkout"])
    # Check "2 weeks" was converted to 14
    assert cleaned_df["Days allowed to borrow"].iloc[0] == 14
