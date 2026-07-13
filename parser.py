import pandas as pd


def read_financial_statement(uploaded_file):
    """
    Reads an uploaded Excel or CSV financial statement
    and returns it as a pandas DataFrame.
    """

    if uploaded_file.name.endswith(".xlsx"):
        data = pd.read_excel(uploaded_file)
    else:
        data = pd.read_csv(uploaded_file)

    return data