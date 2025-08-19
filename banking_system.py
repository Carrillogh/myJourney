# Features
# - Deposit
# - Withdrawal
# - Balance

print("Welcome to GH Bank!\n")

actions = [
    'Deposit',
    'Withdrawal',
    'Balance',
    'Exit'
]

balance = 0

while True:
    for number, action in enumerate(actions, start=1):
        print(f"{number}. {action}")

    # getting to choose your option
    choice = input("Enter your choice(1-4): ")

    # Deposit
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        if amount > 0:
            print(f"Deposited: ${amount:.2f} \nNew balance: ${balance:.2f}")
        else:
            print("Invalid amount. Please enter a positive number.")

    # Withdrawal
    elif choice == '2':
        print(f"${balance:.2f}")
        amount = float(input("Enter amount to withdraw: "))
        if balance < amount:
            print("Not Enough balance")
        else:
            balance > amount
            balance -= amount
            print(f"Withdrawal: ${amount:.2f} \nNew balance: ${balance:.2f}")

    # Balance
    elif choice == '3':
        print(f"Current balance: ${balance:.2f}")

    # Exit
    elif choice == '4':
        print("Thank you for using GH Bank. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
