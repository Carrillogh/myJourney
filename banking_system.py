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

while True:
    for number, action in enumerate(actions, start=1):
        print(f"{number}. {action}")

    # getting to choose your option
    choice = input("Enter your choice: ")

    # Deposit...and because its monetary, we will use float
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid amount. Please enter a positive number.")
