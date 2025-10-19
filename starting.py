while True:
    try:
         operation = input("\nChoose an arithmetic operation (+, -, /, %) or 'quit' to Exit: ")
         if operation.lower() == 'quit':
            break
    except ValueError:
        print("This Operator is Incorrect.")
        continue
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
         print("\nThis Operator is incorrect.")
 
 