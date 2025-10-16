import time
print("<-/Welcome to the Number Guessing Game\\->")
while True:
 
 
 Random_Number = int(time.strftime("%M")) % 100
 try:
  UserInput = int(input("Enter the Number You Guessed : "))
 except ValueError:
    print("Oops! That wasn't a number. Try again.")
    continue
 
 if UserInput == Random_Number:
     print("You Guessed the Correct Number\n")
     break
 elif UserInput > Random_Number:
     print("Your Number is Greater the Actual Number\n")
 elif UserInput < Random_Number:
     print("The Guessed Number is Lower Then The Actual Number\n")
 else:
     print("Its Impossible to Even Trigger This Congrats on How You did it")
    