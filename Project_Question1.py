###Project_1: ATM Simulator


correct_pin = "1234"
attempts = 3
balance = 10000
transactions = []

while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("PIN accepted!")
        break
    else:
        attempts -= 1

        if attempts > 0:
            print(f"Wrong PIN: Attempt left: {attempts}")
        else:
            print("Card bloacked")

if attempts > 0:
    while True:
        print("\n--- ATM MENU ---")
        print("1.Balance")
        print("2.Deposite")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter Your choice: ")

        if choice == "1":
            print("current Balance:", balance)
        elif choice == "2":
            amount = float(input("Enter Deposite amount: "))
            if amount > 0:
                balance += amount
                transactions.append(("Deposite", amount))
                print("New balance:", balance)
            else:
                print("Amount must be above 0.")
        elif choice == "3":
            amount = float(input("Enter Your Withdrawl amount: ")) 
            if amount <= 0:
                print("Amount must be above zero")
            elif amount > balance:
                print("Insuffient balance")
            else:
                balance -= amount
                transactions.append(("withdraw", amount))
                print("New balance:", balance)
        elif choice == "4":
            print("\nTransactions History:")

            for transactions, amount in transactions:
                print(transactions, amount)

            print("Thankyou!")
            break
        else:
            print("invalid choice. Try again.") 


        
