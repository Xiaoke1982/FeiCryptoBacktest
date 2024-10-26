import yfinance as yf
import pandas as pd

def generate_data_yf(output_path, symbol = "ETH-USD",
                     start_date = "2017-01-01", end_date = None,
                     interval = "1d"):
    """
    Fetch cryptocurrency data from Yahoo Finance API, and save it as a CSV file.

    :param output_path: the path where the csv file will be saved
    :param symbol: defauls symbol is ETH-USD
    :param start_date: Start Date (YYYY-MM-DD)
    :param end_date: End Date (YYYY-MM-DD)
    :param interval: time interval ("1d" for daily, "1h" for hourly"
    """

    # If end_date is None, don't pass the end argument, which defaults to today
    if end_date is None:
        
        print(f"fecthing {symbol} data from {start_date} to today with interval {interval}...")
        data = yf.download(symbol, start = start_date, 
                           interval =i nterval)
    else:
        
        print(f"fecthing {symbol} data from {start_date} to {end_date} with interval {interval}...")
        data = yf.download(symbol, 
                           start = start_date, end = end_date, 
                           interval = interval)
    
    # Check if data was successfully fetched
    if data.empty:
        print(f"No data found for {symbol} with the given time range")
        return

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data.to_csv(output_path)
    print(f"data has been saved to {output_path}")


# Save the data to a CSV file
if __name__ == "__main__":
    
    generate_data_yf("../data/eth_daily_data.csv", symbol = "ETH-USD",
                     start_date = "2017-01-01", end_date = None,
                     interval = "1d")
