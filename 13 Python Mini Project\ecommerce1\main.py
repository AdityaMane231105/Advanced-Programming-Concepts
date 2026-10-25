from Products.product import product_info
from Products.price import product_price
from Customers.customers import customer_info
from Customers.address import customer_address
from Orders.orders import order_info
from Orders.status import order_status
from Payments.payment import payment_date, payment_info
from Payments.method import payment_method
 
print(product_info())
print("Price:", product_price())
print(customer_info())
print(customer_address())
print(order_info())
print(order_status())
print(payment_info())
print(payment_method())
print(payment_date())

    