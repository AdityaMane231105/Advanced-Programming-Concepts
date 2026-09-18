from banking import account,transaction,loan
a=account.create(1)
transaction.deposit(a,1000)
transaction.withdraw(a,200)
print(account.get_balance(a))
print(loan.loan(1000,10,2))
