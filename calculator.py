x = float(input("enter your first number: "))
y = float(input("enter your second number: "))
operator = input("enter operator(+,-,*,/): ")
if operator == '+':
    print(f"{x} + {y} = {x+y}")
elif operator == '-':
    print(f"{x} - {y} = {x-y}")
elif operator == '*':
    print(f"{x} * {y} = {x*y}")
elif operator == '/':
    print(f"{x} / {y} = {x/y}")
else:
    print("invalid")
