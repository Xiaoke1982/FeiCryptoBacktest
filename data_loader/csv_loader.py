import pandas as pd


def load_csv_data(file_path, source):
    """
    """
    
    try:
        data = pd.read_csv(file_path, index_col = "Date", parse_dates)