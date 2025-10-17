import time
import random

def Random_guess(Max_Value,low,med,hard):
    if low == 1:
     print("Chooose a Number Between 0 to 59")
     Random_Number = Max_Value
    elif med == 1:
        print("Chooose a Number Between 0 to 59")
        Random_Number = Max_Value
    else:
        print(f"Choose a Number Between 0 to {hard} Its Close to impossible to do this try Your best :)")
        Random_Number = Max_Value
    while True:
  
  
#   Random_Number = int(time.strftime("%M"))
     
     try:
      UserInput = int(input("Enter the Number You Guessed : "))
     except ValueError:
        print("Oops! That wasn't a number. Try again.")
        continue
     
     if UserInput == Random_Number:
         print("You Guessed the Correct Number\n")
         break
     elif UserInput > Random_Number:
         print("Your Number is Greater the Actual Number try again : \n")
     elif UserInput < Random_Number:
         print("The Guessed Number is Lower Then The Actual Number try again : \n")
     else:
         print("Its Impossible to Even Trigger This Congrats on How You did it")



while True:
    
    print("\n<-/Welcome to the Number Guessing Game\\->")
    print("\nChoose a Difficulty")
    Diffculty = input("Enter Here Low Med or Hard Or type 'exit' for Exit : ")

    if Diffculty.lower() == 'low':
       Random_guess(int(time.strftime("%M")),1,0,0)
    elif Diffculty.lower() =='med':
        Random_guess(int(time.strftime("%M")) % 100,0,1,0)
    elif Diffculty.lower() == 'hard':
        Random_guess(random.randint(0,100),0,0,100)
    elif Diffculty.lower() == 'exit':
            print("Exiting...")
            time.sleep(1)
            break
    else:
        print("Oops! You Didnt Entered it Correctly")
        continue
        
    
    