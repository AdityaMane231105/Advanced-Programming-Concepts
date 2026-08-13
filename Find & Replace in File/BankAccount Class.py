class BankAccount:
    counter = 1000 

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.counter += 1
        self.account_number = BankAccount.counter

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_holder} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.account_holder} withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"{self.account_holder} has insufficient funds!")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}, Account Number: {self.account_number}, Balance: {self.balance}")

    def transfer(self, amount, other_account):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print(f"{self.account_holder} transferred {amount} to {other_account.account_holder}.")
        else:
            print(f"{self.account_holder} has insufficient funds for transfer!")

acc1 = BankAccount("Alice")
acc2 = BankAccount("Bob")

acc1.deposit(500)
acc1.withdraw(100)
acc1.transfer(200, acc2)

acc1.display_balance()
acc2.display_balance()
