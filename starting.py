operation = input("Choose an arithmetic operation (+, -, /, %): ")

if operation == '+':
    Num = float(input("Enter the first number: "))
    Num2 = float(input("Enter the second number: "))
    print("There you go:", Num + Num2)
elif operation == '-':
    Num = float(input("Enter the first number: "))
    Num2 = float(input("Enter the second number: "))
    print("There you go:", Num - Num2)
elif operation == '/':
     Num = float(input("Enter the first number: "))
     Num2 = float(input("Enter the second number: "))
     print("There you go:", Num / Num2)
elif operation == '%':
    Num = float(input("Enter the first number: "))
    Num2 = float(input("Enter the second number: "))
    print("There you go:", Num % Num2)
else:
    print("\nThis parameter is incorrect.")

