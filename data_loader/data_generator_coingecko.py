import pandas as pd
from pycoingecko import CoinGeckoAPI
import time


def generate_data_coingecko(output_path, coin_id = "bitcoin", vs_currency = "usd",
                            start_date = "2023-11-01", end_date = "2024-10-01",
                            intervel = "4h"):
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
    
    # Initialize CoinGecko API
    cg = CoinGeckoAPI()

    #Convert start and end dates to Unix timestamp
    from_timestamp = int(time.mktime(pd.to_datetime(start_date).timetuple()))
    to_timestamp = int(time.mktime(pd.to_datetime(end_date).timetuple()))

    #Fetch data from the specific date range
    print(f"Fetching data for {coin_id} from {start_date} to {end_date}...")
    data = cg.get_coin_market_chart_range_by_id(id = coin_id, vs_currency = vs_currency,
                                                from_timestamp = from_timestamp, to_timestamp = to_timestamp)


    # Convert the data to a pandas Data Frame
    df = pd.DataFrame(data["prices"], columns = ["Timestamp", "Price"])
    df["Date"] = pd.to_datetime(df["Timestamp"], unit = "ms")  # Conver Unix Timestamp to data-time value
    df.set_index("Date", inplace = True)  # Set the Date as the index for resampling

    # Resample the data to desired interval
    df_resampled = df.resample(interval).first()

    # Save teh data as a CSV file to the output path
    df_resampled.to_csv(output_path)
    print(f"Data has been saved to {output_path} with {interval} intervals.")
 
    

if __name__ == "__main__":
    generate_data_coingecko("../data/bitcoin_4h_data.csv")