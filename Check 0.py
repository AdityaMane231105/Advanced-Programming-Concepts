def main():
	try:
		n = float(input("Enter a number: ").strip())
	except Exception:
		print("Invalid input")
		return

	if n == 0:
		print("Zero")
	else:
		print("Non-zero")

if __name__ == "__main__":
	main()