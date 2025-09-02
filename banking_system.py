# Features
# - Deposit
# - Withdrawal
# - Balance

print("Welcome to GH Bank!\n")

actions = [
    'Deposit',
    'Withdrawal',
    'Balance',
    'Loan',
    'Exit'
]

balance = 0
balance_history = 0
while True:
    for number, action in enumerate(actions, start=1):
        print(f"{number}. {action}")

    # getting to choose your option
    choice = input("Enter your choice(1-5): ")

    # Deposit
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        if amount < 0:
            print(f"invalid amount")
        else:
            balance += amount
            balance_history += amount
            print(f"Deposited: ${amount:.2f} \nNew balance: ${balance:.2f}")

    # Withdrawal
    elif choice == '2':
        print(f"${balance:.2f}")
        amount = float(input("Enter amount to withdraw: "))
        if balance < amount:
            print("Not Enough balance")
        else:
            if amount < 0:
                print('invalid amount')
            else:
                balance -= amount
                print(
                    f"Withdrawal: ${amount:.2f} \nNew balance: ${balance:.2f}")

    # Balances
    elif choice == '3':
        print(f"Current balance: ${balance:.2f}")

    # Loan
    elif choice == '4':
        required_deposit = 50000
        loan_amount = float(input("Enter loan amount to request: "))
        if balance_history >= required_deposit:
            print('Approved for vetting')
        else:
            print('Denied due to low savings history')

    # Exit
    elif choice == '5':
        print("Thank you for using GH Bank. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
