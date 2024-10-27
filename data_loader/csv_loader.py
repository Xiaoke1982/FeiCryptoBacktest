import pandas as pd


def load_csv_data(file_path, source):
    """
    Load CSV data from a given file path and return it as a pandas Data Frame.
    
    The returned Data Frame only include "Date" and "Close" columns.
    
    @param file_path: the location the csv file is loaded
    @param source: data source ("coingecko" or "yahoo")
    
    @return: a dataframe containing "Date" and "Close" columns
    """
    
    try:
        data = pd.read_csv(file_path, index_col = "Date", parse_dates = True)
        
        if source == "coingecko":
            data.rename(columns = {"Price": "Close"}, inplace = True)
        
        standardized_data = data[["Close"]]
        
        print(f"Successfully standardized and loaded data from {file_path}")
        return standardized_data
        
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
        
        
        
if __name__ == "__main__":
    
    btc_data = load_csv_data(file_path = "../data/bitcoin_4h_data.csv", source = "coingecko")
    
    eth_data = load_csv_data(file_path = "../data/eth_daily_data.csv", source = "yahoo")
    
    print(btc_data.head())
    print(eth_data.tail())