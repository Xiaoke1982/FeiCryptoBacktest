if __name__ == "__main__":
    
    # Step 1
    # load csv data from data/bitcoin_4h_data.csv
    # use the csv_loader.py in data_loader directory to covert the csv data to a df with columns "Date" and "Close"
    from data_loader.csv_loader import load_csv_data
    data = load_csv_data("data/bitcoin_4h_data.csv", source = "coingecko")
    
    
    # Step 2
    # Initialize the strategy object
    from strategies.rsi_strategy import RSIStrategy
    rsi_strategy = RSIStrategy()
    
    
    # Step 3
    #Initialize the backtest engine
    from core.backtest_engine import BacktestEngine
    backtest_engine = BacktestEngine(data, rsi_strategy, initial_cash = 1000)
    
    
    # Step 4
    # run the backtest engine
    backtest_engine.run()
    
    
    # Step 5
    # calculate performance and print it out
    performance = backtest_engine.calculate_performance()
    print(performance)
    