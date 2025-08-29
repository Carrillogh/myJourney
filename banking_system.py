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
max_balance = balance
while True:
    for number, action in enumerate(actions, start=1):
        print(f"{number}. {action}")

    # getting to choose your option
    choice = input("Enter your choice(1-4): ")

    # Deposit
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        if amount < 0:
            print(f"invalid amount")
        else:
            balance += amount
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
        balance_history = [50000]
        loan_amount = float(input("Enter loan amount to request: "))
        if max(balance_history) >= 50000:
            print('approved for vetting')
        else:
            print('Denied due to low savings history')

    # Exit
    elif choice == '5':
        print("Thank you for using GH Bank. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
