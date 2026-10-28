
"""Retail point-of-sale system for processing checkouts and receipts."""

import re
import secrets

# Global state
price_list = {"pen": 10, "notebook": 45, "bag": 799, "bottle": 150}
sales_data = {"total": 0.0}
receipt_lines = []


def process_checkout(cart_items, tax_rate=0.05, receipts=None):
    """Calculate a checkout total and record the receipt."""
    if receipts is None:
        receipts = []

    if not isinstance(tax_rate, (int, float)) or not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1.")

    subtotal = 0.0

    for item, quantity in cart_items:
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise ValueError("Quantity must be a positive integer.")

        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        if item not in price_list:
            raise ValueError(f"Unknown item: {item}")

        subtotal += price_list[item] * quantity

    total = subtotal * (1 + tax_rate)
    receipts.append(total)
    sales_data["total"] += total

    receipt_id = secrets.randbelow(9000) + 1000
    receipt_lines.append(f"Receipt #{receipt_id} total={total:.2f}")

    return total


def apply_promo_code(code_str):
    """Apply a supported arithmetic promo code to total sales."""
    match = re.fullmatch(
        r"\s*total\s*([*+-])\s*(\d+(?:\.\d+)?)\s*",
        code_str,
    )

    if not match:
        raise ValueError("Invalid promo code format.")

    operator, amount_text = match.groups()
    amount = float(amount_text)
    total = sales_data["total"]

    if operator == "*":
        return total * amount

    if operator == "-":
        return total - amount

    return total + amount


def update_stock(item, qty):
    """Validate a stock update request for a known item."""
    if item not in price_list:
        print(f"Unknown item: {item}")
        return

    if not isinstance(qty, int) or isinstance(qty, bool) or qty <= 0:
        raise ValueError("Quantity must be a positive integer.")

    print(f"Stock update requested for {item}: {qty}")


def save_receipt_log(file="pos_log.txt"):
    """Append recorded receipts to the receipt log."""
    with open(file, "a", encoding="utf-8") as receipt_file:
        for line in receipt_lines:
            receipt_file.write(line + "\n")


def print_sales():
    """Display the total sales amount."""
    print(f"Sales so far: {sales_data['total']:.2f}")


def main():
    """Run the retail POS demonstration."""
    print("Bill 1:", process_checkout([("pen", 3), ("notebook", 2)]))
    print("Bill 2:", process_checkout([("bag", 1)]))
    print("Bill 3:", process_checkout([("bottle", 4)]))
    print("Bill 4:", process_checkout([("pen", 2)], tax_rate=0.05))

    update_stock("laptop", 5)

    print("After promo:", apply_promo_code("total * 0.9"))
    code = input("Enter promo code (e.g. total - 50): ") or "total - 50"

    try:
        print("After your promo:", apply_promo_code(code))
    except ValueError as error:
        print(f"Invalid promo code: {error}")

    save_receipt_log()
    print_sales()


if __name__ == "__main__":
    main()
