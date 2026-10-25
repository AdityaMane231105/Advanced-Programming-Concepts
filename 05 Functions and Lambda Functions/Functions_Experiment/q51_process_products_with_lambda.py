products = [
    {"name": "Laptop", "price": 55000, "quantity": 2},
    {"name": "Keyboard", "price": 1500, "quantity": 5},
    {"name": "Notebook", "price": 80, "quantity": 20}
]

product_values = list(map(lambda product: {**product, "total_value": product["price"] * product["quantity"]}, products))
expensive_products = list(filter(lambda product: product["price"] > 1000, product_values))
sorted_products = sorted(product_values, key=lambda product: product["total_value"])
print("Product values:", product_values)
print("Unit price greater than 1000:", expensive_products)
print("Sorted by total value:", sorted_products)
