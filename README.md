# Binance Futures Testnet Trading Bot

## Features
- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- CLI-based input
- Logging system
- Error handling
- Input validation

---

## Setup

### Clone project



git clone <your_repo_url>
cd trading_bot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate
# Install dependencies
pip install -r requirements.txt

## Binance Testnet
Base URL:
https://testnet.binancefuture.com

Generate API keys from Binance Futures Testnet.

## MARKET Order Example
python3 cli.py \
--api_key YOUR_KEY \
--api_secret YOUR_SECRET \
--symbol BTCUSDT \
--side BUY \
--type MARKET \
--quantity 0.001

## LIMIT Order Example

python3 cli.py \
--api_key YOUR_KEY \
--api_secret YOUR_SECRET \
--symbol BTCUSDT \
--side SELL \
--type LIMIT \
--quantity 0.001 \
--price 120000

``` bash

Logs
Logs are stored in:
logs/bot.log



# Project Structure
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── validators.py
│   ├── logging_config.py
│
├── logs/
│   └── bot.log
│
├── cli.py
├── requirements.txt
├── README.md
└── .gitignore


---

## SAVE FILE

Press:
Cmd + S

