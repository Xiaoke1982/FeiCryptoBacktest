from portfolio_manager import PortfolioManager


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
        
        self.portfolio_manager = PortfolioManager(initial_cash)
        
        self.portfolio_value_list = [] #Track portfolio value over time
        
        
    def run(self):
        """
        Generate trading signals and Execute trades based on signals.
        Protfolio value will be recorded over time.
        """
        
        # Generate the trading signals for each close price
        signal_list = self.strategy.generate_signals(self.data)
        
        for i in range(len(self.data)):
            signal = signal_list[i]
            current_price = self.data["Close"].iloc[i]
            
            if signal == 1: # buy signal
                success = self.portfolio_manager.buy(current_price)
                
                if not success:
                    print (f"Failed to buy at {self.data.index[i]}: Insufficient cash.")
                
            elif signal == -1: #sell signal
                success = self.portfolio_manager.sell(current_price)
                
                if not success:
                    print (f"Failed to sell at {self.data.index[i]]}: Insufficient position.")
                
            # calculate current portfolio value   
            current_portfolio_value = self.portfolio_manager.get_portfolio_value(current_price)
            self.portfolio_value_list.append(current_portfolio_value)
            
            
    def get_results(self):
        """
        retrieve the portfolio values over the backtesting period
        
        @return: A list of portfolio values at each time step
        """
        return self.portfolio_value_list
        
        
    
    def calculate_performance(self):
        """
        calculate the total return

        @return: a dictionary that contains total return information
        """
        
        final_value = self.portfolio_value_list[-1]
        
        total_return = (final_value - self.initial_cash) / self.initial_cash
        
        return {"Total Return": total_return}
                
        