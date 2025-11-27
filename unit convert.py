def convert():
    print("1. km to miles")
    print("2. miles to km")
    print("3. kg to pounds")
    print("4. pounds to kg")
    choice = input("Choose option: ")

    x = float(input("Enter value: "))

    if choice == "1":
        print(x * 0.621371)
    elif choice == "2":
        print(x / 0.621371)
    elif choice == "3":
        print(x * 2.20462)
    elif choice == "4":
        print(x / 2.20462)
    else:
        print("Invalid")

convert()
