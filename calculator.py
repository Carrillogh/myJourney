x = float(input("enter num: "))
y = float(input("enter num: "))
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
