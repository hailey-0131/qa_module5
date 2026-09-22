import pandas as pd
import pytest
books = pd.read_csv("library.csv")




# Create a fixture containing the books DataFrame
# This can be reused by multiple tests
@pytest.fixture
def df():
    return books

# Test that the Books column has no trailing spaces
def test_clean_titles_returns_zero_trailing_space(df):

    # Run the clean_titles function using the test DataFrame
    cleaned_df = clean_titles(df)

    # Check that zero book titles end with a space
    assert cleaned_df["Books"].str.endswith(" ").sum() == 0