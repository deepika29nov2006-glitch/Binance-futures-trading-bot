from bot.client import client
from bot.logging_config import logger

def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"Market Order: {order}")
        return order

    except Exception as e:
        logger.error(str(e))
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"Limit Order: {order}")
        return order

    except Exception as e:
        logger.error(str(e))
        raise