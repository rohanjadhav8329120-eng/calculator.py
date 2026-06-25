print("Welcome to the Bank, Please Log in:")
name = input("Enter you'r name: ")
acnum = input("Enter you'r account number: ")
if name == "Rohan":
    if acnum == "8329120893":
        print("Log in successful")
        balance = 5000
        print("1. Check balance")
        print("2. Deposit cash")
        print("3. Exit")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            print("New balance is:", balance)
        elif choice == 2:
            amount = int(input("Please enter amount: "))
            balance = balance + amount
            print("New balance is:", balance)
        elif choice == 3:
            print("Thank you for visiting!")
        elif choice > 3:
            print("Please enter valid choice.")

        # print("Rohan, do you want to check you'r balance? ")
        # choice = input("yes/no: ")
        # if choice == "yes":
        #     print("balance is 5000")
        # else:
        #     print("Thank you!")
    else:
        print("Incorrect Account number")
else:
    print("user does not exist")
