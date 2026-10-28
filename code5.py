def calculator():
	print("Simple Calculator")
	print("Operations: +, -, *, /")

	try:
		first = float(input("Enter the first number: "))
		operation = input("Enter an operation (+, -, *, /): ").strip()
		second = float(input("Enter the second number: "))

		if operation == "+":
			result = first + second
		elif operation == "-":
			result = first - second
		elif operation == "*":
			result = first * second
		elif operation == "/":
			if second == 0:
				print("Error: cannot divide by zero.")
				return
			result = first / second
		else:
			print("Error: unknown operation.")
			return

		print("Result:", result)
	except ValueError:
		print("Error: enter valid numbers.")


if __name__ == "__main__":
	calculator()
