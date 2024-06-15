def calculator():
    print("Welcome to the simple calculator!")

    # Prompt user to input the first number
    num1 = float(input("Enter the first number: "))

    # Prompt user to input the second number
    num2 = float(input("Enter the second number: "))

    # Display operation choices
    print("Choose the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Prompt user to input the operation choice
    choice = input("Enter your choice (1/2/3/4): ")

    # Perform the calculation based on user choice and display the result
    if choice == '1':
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division is: {result}")
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print("Invalid choice! Please select a valid operation.")


# Run the calculator
calculator()
