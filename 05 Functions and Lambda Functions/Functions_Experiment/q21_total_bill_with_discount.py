def total_bill(prices, quantities):
    if len(prices) != len(quantities):
        raise ValueError("prices and quantities must have equal lengths")
    subtotal = sum(price * quantity for price, quantity in zip(prices, quantities))
    discount = subtotal * 0.10 if subtotal >= 5000 else 0
    return subtotal - discount


print(total_bill([1200, 800, 500], [2, 1, 2]))
