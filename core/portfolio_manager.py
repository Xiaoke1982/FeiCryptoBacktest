

class PortfolioManager:
    
    def __init__(self, initial_cash, transaction_fee = 0.001, n_splits = 10):
        
        self.cash_stack = [initial_cash / n_splits] * n_splits
        self.position_stack = []
        
        self.transaction_fee = transaction_fee
        
    
    def buy(self, current_price):
        
        if len(self.cash_stack) > 0:
            
            cash = self.cash_stack.pop()
            shares_to_buy = cash / (current_price * (1 + self.transaction_fee))
            
            self.position_stack.append(shares_to_buy)
            return True
        return False
        
        
    def sell(self, current_price):
        
        if len(self.position_stack) > 0:
            
            shares_to_sell = self.position_stack.pop()
            cash = shares_to_sell * current_price * (1 - self.transaction_fee)
            
            self.cash_stack.append(cash)
            return True
        return False
        
        
    def get_portfolio_value(self, current_price):
        
        return sum(self.cash_stack) + sum(self.position_stack) * current_price
            