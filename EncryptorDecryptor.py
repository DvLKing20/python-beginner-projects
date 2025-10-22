import random
import time

def DECRYPTOR(TO_DECRYPT):
  DECRYPT = list(TO_DECRYPT)
  i = len(TO_DECRYPT)
  if i >= 3:
        RMV = 0
        while RMV < 3:
         RMV += 1
         del DECRYPT[0]
        RMX = 0
        while RMX < 3:
           RMX += 1
           del DECRYPT[-1] 
        REMOVED = DECRYPT.pop(-1)
        DECRYPT.insert(0,REMOVED) 
        return  ''.join(DECRYPT)
  else:
      REMOVED = DECRYPT.pop(-1)
      DECRYPT.insert(0,REMOVED) 
      return ''.join(DECRYPT)

def ENCRYPTOR(TO_ENCRYPT):
    ENCRYPT = list(TO_ENCRYPT)
    i = len(TO_ENCRYPT)
    REMOVED = ENCRYPT.pop(0)
    ENCRYPT.append(REMOVED)    
    if i >= 3:
             for ADD in range(3):
                ADD_THIS = chr(random.randint(97, 122))
                ENCRYPT.append(ADD_THIS)
                for ADDER in range(ADD):
                    ADD_THAT = chr(random.randint(97, 122))
                    ENCRYPT.insert(0,ADD_THAT)
             return  ''.join(ENCRYPT)
    else:
        return ''.join(ENCRYPT)

def TAKING_INPUT():
 while True:
  print("\nEnter the Number Based On What you want to do :")
  print("1: Encryption")
  print("2: Decryption")
  print("0: Exit")
  try:
      CHOSE_CRYPTER = int(input("Enter The Number Here : "))
      if CHOSE_CRYPTER == 1:
         print("\nEnter What you want to Encrypt : ")
         OPERATION_INPUT = input("Enter it Here : ")
         return ENCRYPTOR(OPERATION_INPUT)
      elif CHOSE_CRYPTER == 2:
         print("\nEnter What you want to Decrypt : ")
         OPERATION_INPUT = input("Enter it Here : ")
         return DECRYPTOR(OPERATION_INPUT)
      elif CHOSE_CRYPTER == 0:
         return CHOSE_CRYPTER
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
