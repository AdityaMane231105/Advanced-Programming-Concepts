n = int(input("Enter the number of values: "))
numbers = []

i = 0
while i < n:
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)
    i += 1

if numbers:
    smallest = min(numbers)
    print("The smallest number is:", smallest)
else:
    print("No numbers were entered.")
    
    
    
    
