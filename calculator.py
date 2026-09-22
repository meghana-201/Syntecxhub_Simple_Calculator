def calculate():
    try:
        first_number = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        second_number = float(input("Enter second number: "))

        if operator == "+":
            result = first_number + second_number

        elif operator == "-":
            result = first_number - second_number

        elif operator == "*":
            result = first_number * second_number

        elif operator == "/":
            if second_number == 0:
                print("Error: Cannot divide by zero.")
                return
            result = first_number / second_number

        else:
            print("Invalid operator.")
            return

        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter numbers only.")


while True:
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Calculate")
    print("2. Clear")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculate()

    elif choice == "2":
        print("Calculator cleared.")

    elif choice == "3":
        print("Thank you for using the calculator!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
