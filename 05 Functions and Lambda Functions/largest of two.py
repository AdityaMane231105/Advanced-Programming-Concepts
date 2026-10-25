
def largest_of_two(a, b):
	return a if a >= b else b

if __name__ == "__main__":
	try:
		x = float(input("Enter first number: "))
		y = float(input("Enter second number: "))
	except ValueError:
		print("Please enter valid numbers.")
	else:
		print("Largest:", largest_of_two(x, y))
