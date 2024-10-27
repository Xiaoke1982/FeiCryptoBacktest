import pandas as pd
from pycoingecko import CoinGeckoAPI
import time

def fetch_hourly_data(coin_id, vs_currency, start_date, end_date):
    """
    Fetch hourly cryptocurrency data using the range API from CoinGeckoAPI in chunks of 30 days

    :param coin_id: CoinGecko ID of the cryptocurrency (default is Bitcoin "bitcoin").
    :param vs_currency: The currency in which to get the market data (default is USD "usd").
    :param start_date: The start date for the data (format 'YYYY-MM-DD').
    :param end_date: The end date for the data (format 'YYYY-MM-DD').
    :return: A DataFrame
    """
    
    cg = CoinGeckoAPI()
    df_list = []

    current_start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)

    while current_start < end:
        current_end = current_start + pd.DateOffset(days = 30)

        if current_end > end:
            current_end = end

        from_timestamp = int(current_start.timestamp())
        to_timestamp = int(current_end.timestamp())
                             
        data = cg.get_coin_market_chart_range_by_id(id = coin_id, vs_currency = vs_currency,
                                                from_timestamp = from_timestamp, to_timestamp = to_timestamp)

        df = pd.DataFrame(data["prices"], columns = ["Timestamp", "Price"])
        df["Date"] = pd.to_datetime(df["Timestamp"], unit="ms")
        df.set_index("Date", inplace = True)

        df_list.append(df)

        curent_start = current_end

    
    # Concatenate all dataframes into one dataframe
    return pd.concat(df_list)


def generate_data_coingecko(output_path, coin_id = "bitcoin", vs_currency = "usd",
                            start_date = "2023-11-01", end_date = "2024-10-01",
                            interval = "4h"):
    """
    Fetch cryptocurrency data using the range API from CoinGeckoAPI,
    resample to the desired interval, and save it as a CSV file.

    :param output_path: Path to save the CSV file.
    :param coin_id: CoinGecko ID of the cryptocurrency (default is Bitcoin "bitcoin").
    :param vs_currency: The currency in which to get the market data (default is USD "usd").
    :param start_date: The start date for the data (format 'YYYY-MM-DD').
    :param end_date: The end date for the data (format 'YYYY-MM-DD').
    :param interval: Desired resampling interval (e.g., '4h' for 4-hour intervals).
    """

    # Fetch the hourly data using helper function
    df = fetch_hourly_data(coin_id, vs_currency, start_date, end_date)
    
    # Resample the data to desired interval
    df_resampled = df.resample(interval).first()

    # Save teh data as a CSV file to the output path
    df_resampled.to_csv(output_path)
    print(f"Data has been saved to {output_path} with {interval} intervals.")
 
    

if __name__ == "__main__":
    generate_data_coingecko("../data/bitcoin_4h_data.csv",coin_id = "bitcoin", vs_currency = "usd",
                            start_date = "2023-11-01", end_date = "2024-10-01",
                            interval = "4h")