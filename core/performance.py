import pandas as pd


class Performance:

    @staticmethod
    def calculate_total_return(portfolio_value_list):
        """
        Calculate the total return given the portfolio values over time steps

        @param portfolio_value_list: a list of portfolio values over time

        @return: total return
        """
        initial_value = portfolio_value_list[0]
        final_value = portfolio_value_list[-1]

        return (final_value - initial_value) / initial_value


    @staticmethod
    def calculate_max_drawdown(portfolio_value_list):
        """
        Calculate the max drawdown based on the portfolio values over time

        @param portfolio_value_list: a list of portfolio values over time

        @return: Maximum Drawn
        """
        portfolio_value_series = pd.Series(portfolio_value_list)

        cumulative_max_series = portfolio_value_series.cummax()

        drawdown_series = (portfolio_value_series - cumulative_max_series) / cumulative_max_series

        max_drawdown_value = drawdown_series.min()

        return max_drawdown_value


    @staticmethod
    def calculate_performance(portfolio_value_list):
        """
        Calculate all the performance methods and return a dictionary

        @param portfolio_value_list: a list of portfolio values over time

        @return: a dictionary including Total Return, Max Drawdown, etc...
        """
        return {
            "Total Return": Performance.calculate_total_return(portfolio_value_list),
            "Maximum Drawdown": Performance.calculate_max_drawdown(portfolio_value_list)
        }