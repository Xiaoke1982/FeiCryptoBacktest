

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
        
        
        self.cash_stack = [initial_cash * 0.2] * 5
        self.position_stack = []
        self.portfolio_value_list = []
        
        
    def run(self):
        """
        """
        
        # Generate the trading signals for each close price
        signal_list = self.strategy.generate_signals(self.data)
        
        for i in range(len(self.data)):
            signal = signal_list[i]
            price = self.data["Close"].iloc[i]
            
            if signal == 1 and len(self.cash_stack) > 0:
                cash = self.cash_stack.pop()
                shares_to_buy = cash / price
                
                self.position_stack.append(shares_to_buy)
                
            elif signal == -1 and len(self.position_stack) > 0:
                shares_to_sell = self.position_stack.pop()
                cash = price * shares_to_sell
                
                self.cash_stack.append(cash)
                
                
            current_portfolio_value = sum(self.cash_stack) + sum(self.position_stack) * price
            self.portfolio_value_list.append(current_portfolio_value)
            
            
    def get_results(self):
        
        return self.portfolio_value_list
        
        
    def calculate_performance(self):
        
        final_value = self.portfolio_value_list[-1]
        
        total_return = (final_value - self.initial_cash) / self.initial_cash
        
        return {"Total Return": total_return}
                
        