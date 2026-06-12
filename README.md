# Binance Futures Testnet Trading Bot

A simple Python CLI application that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

## Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL sides
- Command-line interface using argparse
- Input validation
- Structured project architecture
- Logging of API requests and responses
- Exception handling for API and network errors

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── cli.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
├── .env
├── README.md
└── requirements.txt
```

---

## Requirements

- Python 3.9+
- Binance Futures Testnet Account
- Binance Testnet API Key
- Binance Testnet Secret Key

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd trading_bot
```

### Create Virtual Environment

```bash
python -m venv myenv
```

### Activate Virtual Environment

Windows:

```bash
myenv\Scripts\activate
```

Linux / Mac:

```bash
source myenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory.

```env
API_KEY=your_binance_testnet_api_key
API_SECRET=your_binance_testnet_secret_key
```

---

## Binance Testnet URL

The application uses Binance Futures Testnet:

https://testnet.binancefuture.com

---

## Running the Application

### MARKET Order Example

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order Example

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

### SELL MARKET Order

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

---

## Sample Output

### Successful Order

```text
ORDER REQUEST

Symbol : BTCUSDT
Side   : BUY
Type   : MARKET
Qty    : 0.001

SUCCESS

Order ID : 15035074467
Status   : NEW
```

### Error Example

```text
ERROR: APIError(code=-1022): Signature for this request is not valid.
```

---

## Logging

Application logs are stored in the `logs` directory.

Logs include:

- API Requests
- API Responses
- Order Details
- Errors and Exceptions

---

## Validation

The application validates:

- Symbol
- Side (BUY / SELL)
- Order Type (MARKET / LIMIT)
- Quantity
- Price (required for LIMIT orders)

---

## Error Handling

The application handles:

- Invalid user inputs
- Binance API errors
- Authentication errors
- Network failures
- Unexpected exceptions

---

## Assumptions

- User has a valid Binance Futures Testnet account.
- API credentials are correctly configured.
- Internet connection is available.
- Supported order types are MARKET and LIMIT.
- Supported sides are BUY and SELL.

---

## Deliverables Completed

- MARKET Order Placement
- LIMIT Order Placement
- CLI Input Validation
- Logging System
- Error Handling
- Clean Project Structure
- README Documentation

---

## Author

""Deepika pal""

Python Developer Assignment