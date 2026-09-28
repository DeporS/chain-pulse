# ChainPulse

An incremental data engineering project for live cryptocurrency market data and, later, public on-chain events.

## Current scope: v0

Receive ten real BTC/USDT spot trades from Binance's official public WebSocket stream and print their trade time, ID, price, and quantity. This is a connectivity and data-shape check; it does not store events or guarantee recovery from disconnects.

## Run on WSL Ubuntu

Requires Python 3.11 or newer and a network connection.

```bash
python3 --version
sudo apt update
sudo apt install -y python3-venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python chainpulse_v0.py
```

Expected result: `Połączono...` followed by ten lines with fresh UTC timestamps, trade IDs, prices in USDT, and quantities in BTC. Actual market values vary. If the connection fails, retain the traceback for diagnosis.

## Planned stages

| Stage | Focus |
| --- | --- |
| v0 | Read a live trade stream in the terminal |
| v1 | Persist raw trades in PostgreSQL and query per-minute volume |
| v2 | Add Kafka and consumer recovery/replay |
| v3 | Normalize data from another exchange |
| v4 | Add lakehouse layers, quality checks, and monitoring |
| v5 | Add public on-chain events and an analytics interface |

The later stages are a direction, not implemented features. Only measured results will appear as project metrics.

Market data source: [Binance Spot WebSocket Market Streams](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams). This project is a data platform, not a trading bot.
