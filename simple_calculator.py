

def get_number_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation_choice():
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        try:
            choice = int(input("Choose an operation (enter the number): "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Invalid choice. Please enter a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def perform_operation(a, b, operation):
    if operation == 1:
        return a + b
    elif operation == 2:
        return a - b
    elif operation == 3:
        return a * b
    elif operation == 4:
        return a / b


def main():
    print("Welcome to the calculator.")

    while True:
        a = get_number_input("Enter the first number: ")
        b = get_number_input("Enter the second number: ")

        operation = get_operation_choice()

        result = perform_operation(a, b, operation)
        print("Result:", result)

        while True:
            continue_option = input(
                "Do you want to continue? (yes/no): ").lower()
            if continue_option in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if continue_option == "no":
            print("Thank you for using the calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
