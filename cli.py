import argparse

from bot.client import BinanceFuturesClient
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)
from bot.logging_config import setup_logger


logger = setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--api_key", required=True)
parser.add_argument("--api_secret", required=True)
parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    client = BinanceFuturesClient(
        args.api_key,
        args.api_secret
    )

    logger.info(f"Placing {args.type} order")

    if args.type.upper() == "MARKET":
        result = client.place_market_order(
            args.symbol,
            args.side,
            args.quantity
        )

    else:
        if args.price is None:
            raise ValueError("LIMIT order requires --price")

        result = client.place_limit_order(
            args.symbol,
            args.side,
            args.quantity,
            args.price
        )

    logger.info(f"Order response: {result}")

    print("\nORDER SUCCESS")
    print(result)

except Exception as e:
    logger.error(str(e))
    print("\nORDER FAILED")
    print(str(e))