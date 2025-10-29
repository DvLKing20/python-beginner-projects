import os
import time

def MAKE_FILES(USER_PATH,FILE_TYPE,HOW_MANY,NAME):
   try:
    os.chdir(f"{USER_PATH}")
    for i in range(1,HOW_MANY+1):
        open(f"{NAME}{i:02d}.{FILE_TYPE}", 'w')
    print("\nprocessing...")
    time.sleep(.5)
    print("Secussefully Done")
   except Exception:
       print("\nYOU ENTERED SOMETHING WRONG CHECK THE PATH YOU ENTERED AND RUN THE PROGRAM AGAIN!")
def RENAME_FILES(USER_PATH,FILE_TYPE,NAME):
   try:
    os.chdir(f"{USER_PATH}")
    LIST_OF_FILES = os.listdir(f"{USER_PATH}")
    for INDEX, FILES in enumerate(LIST_OF_FILES):
       os.rename(f"{FILES}", f"{NAME}{INDEX+1:02d}.{FILE_TYPE}")
    print("\nprocessing...")
    time.sleep(.5)
    print("Secussefully Done")
   except Exception:
      print("\nYOU ENTERED SOMETHING WRONG CHECK THE PATH YOU ENTERED AND RUN THE PROGRAM AGAIN!")
    
def REMOVE_FILES(USER_PATH):
      try:
          DELETE_FILES = os.listdir(f"{USER_PATH}")
          for FILES in DELETE_FILES:
               os.remove(os.path.join(USER_PATH, FILES))
          print("\nprocessing...")
          time.sleep(.5)
          print("Secussefully Done")
      except Exception:
         print("\nYOU ENTERED SOMETHING WRONG CHECK THE PATH YOU ENTERED AND RUN THE PROGRAM AGAIN!")
while True:
        
    print("\n1: MAKE FILES\n2: RENAME FILES\n3: REMOVE FILES\n0: EXIT")
    try:
        USER_INPUT = int(input("ENTER IT HERE : "))
        if USER_INPUT == 0:
             print("\nExiting...")
             break
        elif USER_INPUT == 3:
             REMOVE_PATH = input("ENTER THE FOLDER PATH HERE(do note it will Remove everything from the Folder): ")
             REMOVE_FILES(REMOVE_PATH)
             continue
        elif USER_INPUT >= 4:
             print("\nSUCH OPERATION DOESNT EXIST")
             continue
    except  ValueError:
            print("\nERROR THATS NOT A NUMBER")
            continue
        
    USER_PATH = input("ENTER THE PATH HERE : ")
    FILE_TYPE = input("ENTER THE FILE TYPE eg(pdf,png,txt etc...): ")
    NAME = input("YOU CAN ENTER NAME IF YOU WANT OR JUST PRESS ENTER : ")
    match USER_INPUT:
         case 1:
              try:
               HOW_MANY = int(input("ENTER HOW MANY FILES TO MAKE : "))
              except :
                 print("\nERROR ENTER A NUMBER")
                 continue
              MAKE_FILES(USER_PATH,FILE_TYPE,HOW_MANY,NAME)
         case 2:
              RENAME_FILES(USER_PATH,FILE_TYPE,NAME)