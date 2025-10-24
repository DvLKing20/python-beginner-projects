import random
import time

def DECODER(TO_DECODE):
  RESULT = []
  ENCODED = TO_DECODE.split(" ")
  for CHECK_LEN in ENCODED:
     CHECK_LIST = list(CHECK_LEN)

     
     if len(CHECK_LIST) >= 3:
           REMOVE = 1
           while REMOVE <= 3:
             del CHECK_LIST[0]
             REMOVE += 1
           REMOVE = 1  
           while REMOVE <= 3:
             del CHECK_LIST[-1]
             REMOVE += 1

           REMOVED = CHECK_LIST.pop(-1)
           CHECK_LIST.insert(0, REMOVED)
           RESULT.append(''.join(CHECK_LIST))
     else:
           REMOVED = CHECK_LIST.pop(-1)        
           CHECK_LIST.insert(0, REMOVED)
           RESULT.append(''.join(CHECK_LIST))
           
      
  return ' '.join(RESULT)

def ENCODER(TO_ENCRYPT):
    RESULT = []
    ENCRYPT = TO_ENCRYPT.split(" ")
    for CHECK_LEN in ENCRYPT:
        
        
        CHECK_LIST = list(CHECK_LEN)
        REMOVED = CHECK_LIST.pop(0)
        CHECK_LIST.append(REMOVED)
        
        if len(CHECK_LIST) >= 3:
    


              for ADD in range(3):
                 #add 3 random chracters at the end one by one
                 ADD_THIS = chr(random.randint(97, 122))
                 CHECK_LIST.append(ADD_THIS)
                 for ADDER in range(ADD):
                    #add 3 random characters front one by one
                    ADD_THAT = chr(random.randint(97, 122))
                    CHECK_LIST.insert(0,ADD_THAT)
              
              RESULT.append(''.join(CHECK_LIST))
        else:
                RESULT.append(''.join(CHECK_LIST))
        
    return ' '.join(RESULT)

def TAKING_INPUT():
 while True:
  print("\nEnter the Number Based On What you want to do :")
  print("1: Encode")
  print("2: Decode")
  print("0: Exit")
  try:
      CHOSE_CODER = int(input("Enter The Number Here : "))
      if CHOSE_CODER == 1:
         print("\nEnter What you want to Encrypt : ")
         OPERATION_INPUT = input("Enter it Here : ")
         return ENCODER(OPERATION_INPUT)
      elif CHOSE_CODER == 2:
         print("\nEnter What you want to Decrypt : ")
         OPERATION_INPUT = input("Enter it Here : ")
         return DECODER(OPERATION_INPUT)
      elif CHOSE_CODER == 0:
         return CHOSE_CODER
  except ValueError:
      print("\nError Please Enter a Valid Number")
while True: 
 OPERATION_COMPLETED = TAKING_INPUT()
 if OPERATION_COMPLETED == 0:
     print("Exiting...")
     time.sleep(1)
     break
 else:
     print("Processing...")
     time.sleep(1)
     print(f"Your Operation Was Completed Here is Your Entered Stuff '{OPERATION_COMPLETED}'\n")
     time.sleep(1)
