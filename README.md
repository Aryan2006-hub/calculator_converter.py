
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


def calculator():
    a = get_number("Enter first number: ")
    op = input("Enter operator (+, -, *, /): ")
    b = get_number("Enter second number: ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Cannot divide by zero!")
    else:
        print("Invalid operator!")


def unit_converter():
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")

    choice = input("Choose conversion: ")

    if choice == "1":
        km = get_number("Enter kilometers: ")
        print("Miles:", round(km * 0.621371, 2))
    elif choice == "2":
        c = get_number("Enter Celsius: ")
        print("Fahrenheit:", round((c * 9/5) + 32, 2))
    else:
        print("Invalid choice!")


def currency_converter():
    amount = get_number("Enter amount: ")
    rate = get_number("Enter exchange rate: ")

    if amount < 0 or rate <= 0:
        print("Amount must be non-negative and rate must be positive.")
    else:
        print("Converted amount:", round(amount * rate, 2))


while True:
    print("\n--- Calculator & Unit Converter ---")
    print("1. Calculator")
    print("2. Unit Converter")
    print("3. Currency Converter")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()
    elif choice == "2":
        unit_converter()
    elif choice == "3":
        currency_converter()
    elif choice == "4":
        print("Thank you for using the program!")
        break
    else:
        print("Invalid choice! Try again.")
