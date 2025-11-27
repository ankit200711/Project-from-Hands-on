print("= Number Analyzer =")

num = int(input("Enter a number: "))

if num > 0:
    print("The number is POSITIVE,")
elif num < 0:
    print("The number is NEGATIVE,")
else:
    print("The number is Zero,")

if num % 2 == 0:
    print("The number is EVEN,")
else:
    print("The number is ODD,")