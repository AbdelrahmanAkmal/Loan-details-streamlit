import dask.dataframe as dd

def Search_For_Matches(target_value):
    """
    Searches for matching Exxon Codes in a Dask DataFrame read from a CSV file.

    Parameters:
    target_value (int): The value to search for in the 'LOAN_ID' column.

    Returns:
    pandas.DataFrame or str: A Pandas DataFrame containing matching rows if found, 'No Match Found' if no matches are found,
    or an error message if an exception occurs during the process.
    """
    try:
        # Read the CSV file
        df = dd.read_csv('train_ctrUa4K.csv', assume_missing=True)
        # Filter only matching row(s) for the target value
        filtered_df = df[df['Loan_ID'] == target_value].compute()
        if not filtered_df.empty:
            # Return matching rows as a dataframe
            return filtered_df
        else:
            # Message to display if no matches are found
            return 'No Match Found'
    except Exception as e:
        # Handle exceptions
        return f'Error while loading data: {e}'