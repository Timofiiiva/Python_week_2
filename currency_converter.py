def currency_converter():
    print("Welcome to the Amazing Currency Converter!")

    while True:
        try:
            amount = float(input("\nEnter the amount of money in dollars: "))
            if amount < 0:
                raise ValueError

            print("\nSelect the target currency for conversion:")
            print("1. Euro")
            print("2. British Pound")
            print("3. Japanese Yen")
            target_currency = int(
                input("\nEnter the number corresponding to the currency: "))

            if target_currency not in [1, 2, 3]:
                raise ValueError

            if target_currency == 1:
                conversion_rate = 0.86  # 1 dollar to euro
                target_currency_name = "euros"
            elif target_currency == 2:
                conversion_rate = 0.73  # 1 dollar to pound
                target_currency_name = "British pounds"
            else:
                conversion_rate = 111.14  # 1 dollar to yen
                target_currency_name = "Japanese yens"

            converted_amount = amount * conversion_rate
            print("\nConversion Result:")
            print(f"{amount:.2f} dollars are equal to {converted_amount:.2f}\
 {target_currency_name}.\n")

            choice = input("Do you want to perform another \
conversion? (yes/no): ").lower()
            if choice != "yes":
                break
        except ValueError:
            print(
                "\nInvalid input. Please enter a valid positive amount and \
choose a valid currency option.")

    print("\nThank you for using the Amazing Currency Converter. Have a great \
day!")


if __name__ == "__main__":
    currency_converter()
