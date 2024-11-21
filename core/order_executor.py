

class OrderExecutor:
    
    def __init__(self, transaction_rate = 0.001, slippage_rate = 0.0001):
        
        self.transaction_rate = transaction_rate
        self.slippage_rate = slippage_rate
        
        
    def buy(self, current_price, cash):
        
        buy_price = current_price * (1 + self.slippage_rate)
        
        shares_to_buy = cash * (1 - self.transaction) / buy_price
        
        return shares_to_buy
        
        
    def sell(self, current_price, shares_to_sell):
        
        sell_price = current_price * (1 - self.slippage_rate)
        
        cash = sell_price * shares_to_sell * (1 - self.transaction_rate)
        
        return cash