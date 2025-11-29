def unit_converter():
    while True:
        print("\n=== Unit Converter ===\n")
        try:
            choice = int(input(
                "Choose the unit to convert:\n"
                "1. Hours to Minutes/Seconds\n"
                "2. Kilograms to Pounds\n"
                "3. Miles to Kilometers\n"
                "4. Inches to Centimeters\n"
                "Enter choice (1-4): "
            ).strip())

            if choice == 1:
                hours = float(input("Enter hours: ").strip())
                sub_choice = int(input("1. To Minutes\n2. To Seconds\nEnter choice: ").strip())
                if sub_choice == 1:
                    print(f"{hours} hours = {hours * 60} minutes")
                elif sub_choice == 2:
                    print(f"{hours} hours = {hours * 3600} seconds")
                else:
                    print("Invalid input.")

            elif choice == 2:
                kg = float(input("Enter weight in kilograms: ").strip())
                pounds = kg * 2.2046226218
                print(f"{kg} kilograms = {pounds:.2f} pounds")

            elif choice == 3:
                miles = float(input("Enter distance in miles: ").strip())
                kilometers = miles * 1.609344
                print(f"{miles} miles = {kilometers:.2f} kilometers")

            elif choice == 4:
                inches = float(input("Enter length in inches: ").strip())
                centimeters = inches * 2.54
                print(f"{inches} inches = {centimeters:.2f} centimeters")

            else:
                print("Invalid choice. Please choose between 1 and 4.")

        except ValueError:
            print("Please enter valid numeric input.")

        again = input("\nConvert again? (y/n): ").strip().lower()
        if again != "y":
            print("\nProgram ended. Goodbye!")
            break
if __name__ == "__main__":
    unit_converter()
