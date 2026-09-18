from products import list,stock
from customers import info,address
from orders import create,status
from payments import process,history

customer = info.customer()
product = list.all_products()[0]
print(create.create_order(customer,product))
print(process.pay(5000))
print(status.status("O123"))
print("Payment history:", history.history())    

