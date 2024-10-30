if __name__ == "__main__":

    # load csv data from data/bitcoin_4h_data.csv
    # use the csv_loader.py in data_loader directory to covert the csv data to a df with columns "Date" and "Close"
    from data_loader.csv_loader import load_csv_data
    data = load_csv_data("data/bitcoin_4h_data.csv", source = "coingecko")