transactions = [
    ["deposit", 10000],
    ["withdrawal", 2000],
    ["deposit", 5000],
    ["withdrawal", 1500]
]

with open("transactions.txt", "w") as f:
    for t, amount in transactions:
        f.write(f"{t},{amount}\n")

deposits = sum(amount for t, amount in transactions if t == "deposit")
withdrawals = sum(amount for t, amount in transactions if t == "withdrawal")
balance = deposits - withdrawals
largest = max(transactions, key=lambda x: x[1])

print("Total deposits:", deposits)
print("Total withdrawals:", withdrawals)
print("Final balance:", balance)
print("Largest transaction:", largest)

