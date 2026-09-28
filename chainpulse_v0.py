"""Pierwszy krok ChainPulse: odbierz 10 transakcji BTC/USDT na żywo."""

import json
from datetime import datetime, timezone

from websockets.sync.client import connect


STREAM_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"


def main() -> None:
    with connect(STREAM_URL, open_timeout=10) as websocket:
        print("Połączono. Odbieram 10 transakcji BTC/USDT...")

        for _ in range(10):
            trade = json.loads(websocket.recv())
            traded_at = datetime.fromtimestamp(trade["T"] / 1000, tz=timezone.utc)

            print(
                f"{traded_at:%Y-%m-%d %H:%M:%S.%f} UTC | "
                f"id={trade['t']} | "
                f"cena={trade['p']} USDT | "
                f"ilość={trade['q']} BTC"
            )


if __name__ == "__main__":
    main()
