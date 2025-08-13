fast= input("Write the first number: ")
operator = input("Write the operator (+,-,*,/): ")
second = input("Write the second number: ") 

fast = int(fast)
second = int(second)

if operator == "+":
    print(fast + second)
elif operator == "-":
    print(fast - second)
elif operator == "*":
    print(fast * second)
elif operator == "/":
    if second == 0:
        print("Error: Division by zero.")
    else:
        print(fast / second)
else:
    print("Invalid operator.")
