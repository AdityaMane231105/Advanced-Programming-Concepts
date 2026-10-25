balance = 1000.0
transactions = []


def deposit(amount):
    global balance
    if amount <= 0:
        raise ValueError("deposit must be positive")
    balance += amount
    transactions.append(("Deposit", amount, balance))
    return balance


def withdraw(amount):
    global balance
    if amount <= 0:
        raise ValueError("withdrawal must be positive")
    if amount > balance:
        return False
    balance -= amount
    transactions.append(("Withdrawal", amount, balance))
    return True


def balance_enquiry():
    return balance


def transaction_history():
    return transactions.copy()


deposit(500)
withdraw(200)
print("Balance:", balance_enquiry())
print("Transactions:", transaction_history())
