class BankAccount:
    counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.counter += 1
        self.account_number = BankAccount.counter

    def deposit(self, amount):
        self.balance += amount
        print(self.account_holder, "deposited", amount, "New balance:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(self.account_holder, "withdrew", amount, "New balance:", self.balance)
        else:
            print(self.account_holder, "has insufficient funds!")

    def display_balance(self):
        print("Account Holder:", self.account_holder,
              "Account Number:", self.account_number,
              "Balance:", self.balance)

    def transfer(self, amount, other_account):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print(self.account_holder, "transferred", amount, "to", other_account.account_holder)
        else:
            print(self.account_holder, "has insufficient funds for transfer!")


name1 = input("Enter name for first account holder: ")
name2 = input("Enter name for second account holder: ")

acc1 = BankAccount(name1)
acc2 = BankAccount(name2)

deposit_amount = int(input(f"Enter deposit amount for {acc1.account_holder}: "))
acc1.deposit(deposit_amount)

withdraw_amount = int(input(f"Enter withdrawal amount for {acc1.account_holder}: "))
acc1.withdraw(withdraw_amount)

transfer_amount = int(input(f"Enter transfer amount from {acc1.account_holder} to {acc2.account_holder}: "))
acc1.transfer(transfer_amount, acc2)

acc1.display_balance()
acc2.display_balance()
