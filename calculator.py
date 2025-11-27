print ("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Percentage
6. Square Root
7. Area of Square
8. Perimeter of Square
9. Area of Rectangle
10. Perimeter of Rectangle
11. Exit
""")

choice = input("Enter Your Choice : ")

if choice == "1":
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    print("Addition is", num1 + num2)

elif choice == "2":
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    print("Subtraction is", num1 - num2)

elif choice == "3":
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    print("Multiplication is", num1 * num2)
    
elif choice == "4":
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    print("Division is", num1 / num2)

elif choice == "5":
    total = float(input("Enter total value: "))
    part = float(input("Enter part value: "))
    percentage = (part / total) * 100
    print("Percentage =", percentage, "%")

elif choice == "6":
    num = float(input("Enter number: "))
    print("Square Root =", math.sqrt(num))
    
elif choice == "7":
    side = float(input("Enter side of square: "))
    print("Area of Square =", side * side)

elif choice == "8":
    side = float(input("Enter side of square: "))
    print("Perimeter of Square =", 4 * side)

elif choice == "9":
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    print("Area of Rectangle =", length * width)

elif choice == "10":
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    print("Perimeter of Rectangle =", 2 * (length + width))


elif choice == "11":
    print("Exit selected")

else:
    print("Invalid")