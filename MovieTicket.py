age = int(input("Enter your age: "))
ticket = input("Do you have a ticket? (yes/no): ").lower()

if age >= 18:
    if ticket == "yes":
        print("You are allowed to watch the movie.")
    else:
        print("You need a ticket to watch the movie.")
else:
    parents = input("Are your parents with you? (yes/no): ").lower()
    if ticket == "yes" and parents == "yes":
        print("You are allowed to watch the movie with your parents.")
    else:
        print("You are NOT allowed to watch the movie because you are under 18.")