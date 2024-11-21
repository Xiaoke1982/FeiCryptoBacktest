from core.portfolio_manager import PortfolioManager
from core.performance import Performance


class BacktestEngine:
    
    def __init__(self, data, strategy, initial_cash = 1000):
        """
        Initialize Backtest Engine Object
        
        @param data: a data frame with columns of "Date" and "Close", it's genrated by csv_loader in data_loader directory
        @param strategy: a strategy object (e.g. RSIStrategy object)
        @param initial_cash: default 1000
        """
        
        self.data = data
        self.strategy = strategy
        self.initial_cash = initial_cash
        
        # Initialize the portfolio manager object, it will hand buy, sell trading action and calculate portfolio value at each time step
        self.portfolio_manager = PortfolioManager(initial_cash)
        
        self.portfolio_value_list = [] #Track portfolio value over time
        
        
    def run(self):
        """
        Generate trading signals and Execute trades based on signals.
        Protfolio value will be recorded over time.
        """
        
        print(f"Backtesting from {self.data.index[0]} to {self.data.index[len(self.data)-1]}...")
        
        # Generate the trading signals for each close price
        signal_list = self.strategy.generate_signals(self.data)
        
        for i in range(len(self.data)):
            signal = signal_list[i]
            current_price = self.data["Close"].iloc[i]
            
            if signal == 1: # buy signal
                success = self.portfolio_manager.buy(current_price)  # returns if the buy action is successful or not
                
                if not success:
                    print(f"Failed to buy at {self.data.index[i]}: Insufficient cash.")
                else:
                    print(f"Buy at {self.data.index[i]} at price {current_price}")
                
            elif signal == -1: #sell signal
                success = self.portfolio_manager.sell(current_price)  # returns if the sell action is successful or not
                
                if not success:
                    print(f"Failed to sell at {self.data.index[i]}: Insufficient position.")
                else:
                    print(f"Sell at {self.data.index[i]} at price {current_price}")
            # calculate current portfolio value   
            current_portfolio_value = self.portfolio_manager.get_portfolio_value(current_price)
            #print(current_portfolio_value)
            self.portfolio_value_list.append(current_portfolio_value)
            
            
    def get_performance_metrics(self):
            """
            get performance metrics using performance.py mehtods
        
            @return: a dictionary that contains performance metrics
            """
        
            return Performance.calculate_performance(self.portfolio_value_list)
        