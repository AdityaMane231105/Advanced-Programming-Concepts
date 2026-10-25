def deposit(account, amount):
    account["balance"] += amount
 
def withdraw(account, amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
        return True
    return False
