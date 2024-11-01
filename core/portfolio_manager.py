

class PortfolioManager:
    
    def __init__(self, initial_cash, transaction_fee = 0.001, n_splits = 10):
        """
        Initialize the PortfolioManager object instance
        
        @param initial_cash: initial cash
        @param transaction_fee: transaction cost rate, default is 0.1%
        @param n_splits: the number of portions to split the initial cash into for cash stack, default is 10
        """
        
        # split the initial cash into equal portions for cash stack
        self.cash_stack = [initial_cash / n_splits] * n_splits
        self.position_stack = []  #Initialize an empty position stack
        
        self.transaction_fee = transaction_fee
        
    
    def buy(self, current_price):
        """
        Execute a buy operation given current price, update the cash stack and the position stack
        
        @param current_price: current buy price
        
        @return: True if buy successful, False otherwise
        """
        
        if len(self.cash_stack) > 0:  # check if cash is enough for buy action
            
            cash = self.cash_stack.pop() # pop one portion of cash from the cash stack
            shares_to_buy = cash / (current_price * (1 + self.transaction_fee))  #calculate how many shares can be bought
            
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
            cash = shares_to_sell * current_price * (1 - self.transaction_fee)  # sell the position and get the cash
            
            self.cash_stack.append(cash)  #update the cash stack by pushing the cash into it
            return True
        return False
        
        
    def get_portfolio_value(self, current_price):
        """
        Calculate current portfolio value given current price
        
        @return: current portfolio value
        """
        
        return sum(self.cash_stack) + sum(self.position_stack) * current_price
            