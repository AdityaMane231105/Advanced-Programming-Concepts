balance=0
def create(acc): return {'id':acc,'balance':0}
def get_balance(acc): return acc['balance']
def deposit(acc, amount): acc['balance'] += amount
def withdraw(acc, amount):
    if acc['balance'] >= amount:
        acc['balance'] -= amount
    else:
        print("Insufficient funds") 
        