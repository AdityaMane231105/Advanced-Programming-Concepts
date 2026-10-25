inventory = {}

def add_product(name, qty):
    inventory[name] = qty

def update_product(name, qty):
    if name in inventory:
        inventory[name] = qty

def highest_stock():
    return max(inventory, key=inventory.get)

def remove_product(name):
    if name in inventory and inventory[name] == 0:
        del inventory[name]

def total_products():
    return len(inventory)

add_product("Apples", 50)
add_product("Bananas", 30)
update_product("Apples", 60)
remove_product("Bananas")
print("Highest stock:", highest_stock())
print("Total products:", total_products())
