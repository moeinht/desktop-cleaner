def calculate(a, b, operation):
    if operation == 1:
        symbol = "+"
        calculation = a + b
    elif operation == 2:
        symbol = "-"
        calculation = a - b
    elif operation == 3:
        symbol = "*"
        calculation = a * b
    elif operation == 4:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        symbol = "/"
        calculation = a / b
    else:
        raise ValueError("Invalid operation. Choose 1, 2, 3, or 4.")

    return calculation, f"{a} {symbol} {b} = {calculation}"


def getCalculationInputs():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = int(input("Enter your choice (1-4): "))

    return a, b, operation


while True:
    try:
        a, b, operation = getCalculationInputs()

        result, textOpration = calculate(a, b, operation)
        print(f"{textOpration}")

    except ValueError as error:
        print(f"Input error: {error}")

    except ZeroDivisionError as error:
        print(f"Math error: {error}")

    again = input("\nCalculate again? (y/n): ").strip().lower()

    if again != "y":
        print("Goodbye!")
        break
