pin = "1234"
balance = 5000
attempts = 0

while attempts < 3:
    entered_pin = input("Enter PIN: ")
    if entered_pin == pin:
        print("Login Successful")
        print("Your Balance:", balance)
        amt = int(input("Enter amount to withdraw: "))
        if amt <= balance:
            balance -= amt
            print("Transaction Successful")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance")
        break
    else:
        attempts += 1
        print("Wrong PIN")

if attempts == 3:
    print("Your account is blocked")
