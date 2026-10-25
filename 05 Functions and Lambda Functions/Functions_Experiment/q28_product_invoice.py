products = {}


def add_product(name, price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("price and quantity must be non-negative")
    products[name] = {"price": price, "quantity": quantity}


def remove_product(name):
    return products.pop(name, None) is not None


def calculate_subtotal():
    return sum(item["price"] * item["quantity"] for item in products.values())


def apply_coupon(subtotal, coupon_rate):
    return subtotal * coupon_rate


def calculate_gst(taxable_amount, gst_rate):
    return taxable_amount * gst_rate


def generate_invoice(coupon_rate=0.0, gst_rate=0.18):
    subtotal = calculate_subtotal()
    discount = apply_coupon(subtotal, coupon_rate)
    taxable_amount = subtotal - discount
    gst = calculate_gst(taxable_amount, gst_rate)
    return {"products": products.copy(), "subtotal": subtotal, "discount": discount, "GST": gst, "total": taxable_amount + gst}


add_product("Keyboard", 1200, 1)
add_product("Mouse", 600, 2)
print(generate_invoice(coupon_rate=0.10))
