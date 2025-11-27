age = int(input("Enter your age: "))
ticket = input("Do you have a ticket? (yes/no): ")

if age >= 18 and ticket.lower() == "yes":
    print("You are allowed to watch the movie")
elif age < 18:
    print("You are not allowed to watch the movie")
else:
    print("You need a ticket to watch the movie")
