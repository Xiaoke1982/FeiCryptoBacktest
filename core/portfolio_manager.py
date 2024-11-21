from core.order_executor import OrderExecutor

class PortfolioManager:
    
    def __init__(self, initial_cash, transaction_rate = 0.001, slippage_rate = 0.0001, n_splits = 10):
        """
        Initialize the PortfolioManager object instance
        
        @param initial_cash: initial cash
        @param transaction_rate: transaction cost rate, default is 0.1%
        @param slippage_rate: slippage rate default is 0.01%
        @param n_splits: the number of portions to split the initial cash into for cash stack, default is 10
        """
        
        # split the initial cash into equal portions for cash stack
        self.cash_stack = [initial_cash / n_splits] * n_splits
        self.position_stack = []  #Initialize an empty position stack
        
        self.order_executor = OrderExecutor(transaction_rate, slippage_rate)
    
    def buy(self, current_price):
        """
        Execute a buy operation given current price, update the cash stack and the position stack
        
        @param current_price: current buy price
        
        @return: True if buy successful, False otherwise
        """
        
        if len(self.cash_stack) > 0:  # check if cash is enough for buy action
            
            cash = self.cash_stack.pop() # pop one portion of cash from the cash stack
            shares_to_buy = self.order_executor.buy(current_price, cash) # execute buy order
            
            self.position_stack.append(shares_to_buy) # update the position stack by pushing the newly bought shares
            return True
        return False
        
        
    def sell(self, current_price):
        """
        Execute sell operation given current price, update the cash stack and the position stack
        
        @param current_price: current sell price
        
        @return: True if sell successful, False otherwise
        """
        
        if len(self.position_stack) > 0:  # check if there's enough position to sell
            
            shares_to_sell = self.position_stack.pop()  #pop one portion of the position from the position stack
            cash = self.order_executor.sell(current_price, shares_to_sell)  # execute sell order
          
            self.cash_stack.append(cash)  #update the cash stack by pushing the cash into it
            return True
        return False
        
        
    def get_portfolio_value(self, current_price):
        """
        Calculate current portfolio value given current price
        
        @return: current portfolio value
        """
        
        return sum(self.cash_stack) + sum(self.position_stack) * current_price
            