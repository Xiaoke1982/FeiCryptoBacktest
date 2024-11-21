

class OrderExecutor:
    
    def __init__(self, transaction_rate = 0.001, slippage_rate = 0.0001):
        """
        Initialize the OrderExecutor with slippage and transaction rates.

        @param transaction_rate: Transaction rate as a decimal (e.g., 0.001 for 0.1%).
        @param slippage_rate: Slippage rate as a decimal (e.g., 0.0001 for 0.01%).
        """
        self.transaction_rate = transaction_rate
        self.slippage_rate = slippage_rate
        
        
    def buy(self, current_price, cash):
        """
        Execute a buy order with a given cash amount.

        @param current_price: The market price before slippage.
        @param cash: The cash amount available for buying.
        
        @return shares_to_buy: the shares bought
        """
        #Adjust price for slippage
        buy_price = current_price * (1 + self.slippage_rate)
        
        shares_to_buy = cash * (1 - self.transaction_rate) / buy_price
        
        return shares_to_buy
        
        
    def sell(self, current_price, shares_to_sell):
        """
        Execute a sell order with a given shares amount.

        @param current_price: The market price before slippage.
        @param shares_to_sell: The shares amount available for selling.
        
        @return cash: the cash after selling the given shares
        """
        #Adjust price for slippage
        sell_price = current_price * (1 - self.slippage_rate)
        
        cash = sell_price * shares_to_sell * (1 - self.transaction_rate)
        
        return cash