import time
import random

def Random_guess(Max_Value,low,med):
    if low == 'low':
     print("Chooose a Number Between 0 to 59")
     Random_Number = Max_Value
    elif med == 'med':
        print("Chooose a Number Between 0 to 59")
        Random_Number = Max_Value
    else:
        print(f"Choose a Number Between 0 to 100 Its Close to impossible to do this try Your best :)")
        Random_Number = Max_Value
    i = 0
    while True:

#   Random_Number = int(time.strftime("%M"))
     
     try:
      UserInput = int(input("Enter the Number You Guessed or Enter 9999 to Exit: "))
     except ValueError:
        print("Oops! That wasn't a number. Try again.")
        continue
     
     if UserInput == Random_Number:
         print("You Guessed the Correct Number\n")
         print(f"Total Tries = {i}")
         break
     elif UserInput == 9999:
           print(f"Total Tries = {i}")
           print(f"Exiting...")
           time.sleep(1)
           break
     elif UserInput > Random_Number:
         print("Your Number is Greater the Actual Number try again : \n")
         i+=1
     elif UserInput < Random_Number:
         print("The Guessed Number is Lower Then The Actual Number try again : \n")
         i+=1
     else:
         print("Its Impossible to Even Trigger This Congrats on How You did it")



while True:

    print("\n<-/Welcome to the Number Guessing Game\\->")
    print("\nChoose a Difficulty")
    Diffculty = input("Enter Here Low Med or Hard Or type 'exit' for Exit : ").lower()

    if Diffculty == 'low':
       Random_guess(int(time.strftime("%M")),'low','0')
    elif Diffculty=='med':
        Random_guess(int(time.strftime("%M"))%100,'0','med')
    elif Diffculty == 'hard':
        Random_guess(random.randint(0,100),0,0)
    elif Diffculty == 'exit':
            print("Exiting...")
            time.sleep(1)
            break
    else:
        print("Oops! You Didnt Entered it Correctly")
        continue
