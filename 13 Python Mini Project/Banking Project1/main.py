from banking.account import create_account, get_balance
from banking.transaction import deposit, withdraw
from banking.loan import loan_amount
 
account = create_account("Amit", 10000)
deposit(account, 5000)
withdraw(account, 2000)
 
print("Balance:", get_balance(account))
print("Loan amount:", loan_amount(50000, 5, 2))
