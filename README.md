# FeiCryptoBacktest

## Overview
**FeiCryptoBacktest** is a modular Python framework designed for backtesting cryptocurrency trading strategies. It includes tools for portfolio management, strategy integration, and performance evaluation, and supports CSV data loading, making it an ideal platform for building and testing crypto trading strategies.

## Project Structure
The project follows a modular structure to enhance reusability and maintainability. Below is an overview of the main folders and their contents:

- **`core/`**: Contains the core backtesting logic.
  - `backtest_engine.py`: Manages the backtesting workflow by coordinating strategies, data, and portfolio management.
  - `portfolio_manager.py`: Manages cash, positions, and calculates returns.
  - `performance.py`: Provides tools to evaluate performance metrics such as returns, risk, and drawdown.
  - `order_executor.py`: Simulates order execution, including handling slippage and fees.

- **`data_loader/`**: Modules for loading and processing data.
  - `yahoo_loader.py`: Loads data from Yahoo Finance.
  - `csv_loader.py`: Loads data from local CSV files.
  - `data_cleaner.py`: Cleans and preprocesses the data before use.

- **`strategies/`**: Houses different trading strategies.
  - `strategy_base.py`: Base class for all strategies, with essential methods.
  - `rsi_strategy.py`: An example strategy based on the Relative Strength Index (RSI).
  - `macd_strategy.py`: An example strategy based on the Moving Average Convergence Divergence (MACD).

- **`tests/`**: Testing modules to ensure code reliability and stability.
  - `test_backtest_engine.py`: Unit tests for the backtesting engine.
  - `test_portfolio_manager.py`: Unit tests for the portfolio manager.
  - `test_strategy.py`: Unit tests for different strategies.

- **`data/`**: Folder for storing raw historical data.
  - `bitcoin_4h_data.csv`: Example data file with 4-hour interval data for Bitcoin.
  - `eth_daily_data.csv`: Example data file with daily interval data for Ethereum.

- **`notebooks/`**: Jupyter notebooks for running examples or analysis.

## Installation
### Prerequisites
Ensure you have **Python** installed, ideally within a **Conda environment**. To set up the environment, run:

```bash
conda create -n fei_crypto_backtest python=3.9
conda activate fei_crypto_backtest
```

### Install Required Packages

Install all dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```
## Quick Start

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Xiaoke1982/FeiCryptoBacktest.git
    cd FeiCryptoBacktest
    ```

2. **Run an example backtest**:  
   In a Python script or Jupyter Notebook, load your data, set up the strategy, and run the backtest:

    ```python
    from core.backtest_engine import BacktestEngine
    from data_loader.csv_loader import CSVLoader
    from strategies.rsi_strategy import RSIStrategy

    # Load data
    data = CSVLoader('data/bitcoin_4h_data.csv').load_data()

    # Set up strategy
    strategy = RSIStrategy(data)

    # Run backtest
    engine = BacktestEngine(strategy)
    results = engine.run_backtest()
    print(results)
    ```

3. **View results**:  
   Review backtest results and performance metrics in the console or export them for further analysis.

## Usage Guide

### Data Loading

Data loaders are available in `data_loader/`, allowing you to import CSV data or load from Yahoo Finance. Configure your data path and ensure data is cleaned and ready for backtesting.

### Strategy Integration

Strategies should inherit from `strategy_base.py`. Implement custom logic for each strategy by defining buy/sell signals based on your chosen indicators.

### Running Backtests

Use `BacktestEngine` from `core/` to run backtests. The engine coordinates with your strategy, manages positions, and records trades.

### Performance Evaluation

Performance metrics can be calculated using tools in `performance.py`. Use these metrics to evaluate and compare strategy outcomes.

## Example

Here’s an example of running an RSI-based strategy on Bitcoin 4-hour data:

```python
from core.backtest_engine import BacktestEngine
from data_loader.csv_loader import CSVLoader
from strategies.rsi_strategy import RSIStrategy

# Load data
data = CSVLoader('data/bitcoin_4h_data.csv').load_data()

# Set up RSI strategy
strategy = RSIStrategy(data, rsi_period=14, rsi_overbought=70, rsi_oversold=30)

# Initialize backtest engine
engine = BacktestEngine(strategy)

# Run backtest
results = engine.run_backtest()
print(results)
```
## API Documentation

### Core Classes and Methods

- **`BacktestEngine`**: Orchestrates the backtesting process.
  - `run_backtest()`: Runs the backtest and returns results.
- **`PortfolioManager`**: Manages the portfolio, including cash and positions.
  - `update_position()`: Updates position based on strategy signals.
- **`RSIStrategy`** (inherits from `StrategyBase`): Implements an RSI-based trading strategy.
  - `generate_signals()`: Generates buy/sell signals based on RSI levels.

## Testing and Debugging

Run tests in the `tests/` directory to ensure all modules work as expected:

```bash
python -m unittest discover -s tests
```
## Contributing

Contributions are welcome! If you’d like to improve FeiCryptoBacktest, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.
