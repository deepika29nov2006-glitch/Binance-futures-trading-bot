import argparse

from bot.validators import validate_order
from bot.orders import place_market_order, place_limit_order


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\nORDER REQUEST")
        print("----------------")
        print(f"Symbol : {args.symbol}")
        print(f"Side   : {args.side}")
        print(f"Type   : {args.type}")
        print(f"Qty    : {args.quantity}")

        if args.type == "LIMIT":
            print(f"Price  : {args.price}")

        if args.type == "MARKET":
            response = place_market_order(
                args.symbol,
                args.side,
                args.quantity
            )
        else:
            response = place_limit_order(
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )

        print("\nSUCCESS")
        print("----------------")
        print("Order ID :", response.get("orderId"))
        print("Status   :", response.get("status"))

    except Exception as e:
        print("ERROR:", e)


if __name__ == "__main__":
    main()