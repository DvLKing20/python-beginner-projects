import shutil
import os
import time

class USER_CHOICE:
    def __init__(self,USER_PATH,FILE_TYPE,CUSTOM_NAME,HOW_MANY):
        self.USER_PATH = USER_PATH
        self.FILE_TYPE = FILE_TYPE
        self.CUSTOM_NAME = CUSTOM_NAME
        self.HOW_MANY = HOW_MANY

    def MAKE_FOLDERS(self):
       try:
           print("\nprocessing...")
           time.sleep(.2)
           os.chdir(self.USER_PATH)
           for folder in range(int(self.HOW_MANY)):
              os.mkdir(os.path.join(self.USER_PATH,self.CUSTOM_NAME,f"{folder+1:02d}"))
           print("Secussefully Done")
       except Exception:
          print("\nYOU ENTERED SOMETHING WRONG CHECK THE PATH YOU ENTERED AND RUN THE PROGRAM AGAIN!")
    
    def COPY_EVERTHING(self):
          try:
            print("\nprocessing...")
            time.sleep(.2)
            custom_path = os.path.join(self.FILE_TYPE,self.CUSTOM_NAME)
            for COPIES in range(int(self.HOW_MANY)):
             shutil.copytree(f"{self.USER_PATH}",f"{custom_path}{COPIES+1:02d}", dirs_exist_ok=True)
            print("Secussefully Done")
          except Exception:
               print("\nYOU ENTERED SOMETHING WRONG CHECK THE PATH YOU ENTERED AND RUN THE PROGRAM AGAIN!")
    
    def MAKE_FILES(self):
       try:
        print("\nprocessing...")
        time.sleep(.5)
        os.chdir(f"{self.USER_PATH}")
        for i in range(1,int(self.HOW_MANY)+1):
           f = open(f"{self.CUSTOM_NAME}{i:02d}.{self.FILE_TYPE}", 'w')
           f.close()
        print("Secussefully Done")
       except Exception:
           print("\nYOU ENTERED SOMETHING WRONG CHECK THE PATH YOU ENTERED AND RUN THE PROGRAM AGAIN!")
    
    def RENAME_FILES(self):
         try:
          print("\nprocessing...")
          time.sleep(.2)
          os.chdir(f"{self.USER_PATH}")
          LIST_OF_FILES = os.listdir(f"{self.USER_PATH}")
          for INDEX, FILES in enumerate(LIST_OF_FILES):
             if FILES.endswith(f"{self.HOW_MANY}"):
                os.rename(f"{FILES}", f"{self.CUSTOM_NAME}{INDEX+1:02d}.{self.FILE_TYPE}")
             else:
                   continue
          print("Secussefully Done")
         except Exception:
            print("\nYOU ENTERED SOMETHING WRONG CHECK THE PATH YOU ENTERED AND RUN THE PROGRAM AGAIN!")

    def REMOVE_FILES(self):
      try:
          print("\nprocessing...")
          time.sleep(.2)
          DELETE_FILES = os.listdir(f"{self.USER_PATH}")
          for FILES in DELETE_FILES: 
               os.remove(os.path.join(self.USER_PATH, FILES))
          print("Secussefully Done")     
      except Exception:
         print("\nYOU ENTERED SOMETHING WRONG CHECK THE PATH YOU ENTERED AND RUN THE PROGRAM AGAIN!")

while True:
    print("\n1: MAKE FILES\n2: RENAME FILES\n3: REMOVE FILES\n4: COPY FOLDER\n5: MAKE FOLDERS\n0: EXIT\n")
    try:
        USER_INPUT = int(input("ENTER IT HERE : "))
        if USER_INPUT == 0:
              print("\nExiting...")
              break
        USER_PATH = input("ENTER THE PATH HERE (skip Everything after if removing files): ")
        FILE_TYPE = input("FILE TYPE YOU WANT TO RENAME OR MAKE eg(pdf,png,txt etc...or custom path for folders to be Copied(skip if making folders or second Path if copying)) : ") or ""
        HOW_MANY =  input("HOW MANY FILES OR FOLDER TO MAKE OR COPY (if Renaming files Enter Which eg(pdf,png,txt etc...) type you are renaming) : ") or 0
        CUSTOM_NAME = input("YOU CAN ENTER FIRST NAME IF YOU WANT OR JUST PRESS ENTER : ")
        REFERENCE = USER_CHOICE(USER_PATH,FILE_TYPE,CUSTOM_NAME,HOW_MANY)  
        match USER_INPUT:
         case 1:            
               REFERENCE.MAKE_FILES()
         case 2:
              REFERENCE.RENAME_FILES()
         case 3:
                REFERENCE.REMOVE_FILES()
         case 4:
               REFERENCE.COPY_EVERTHING()
         case 5:
              REFERENCE.MAKE_FOLDERS()
    except ValueError:
          print("\nError Thats Not a Number")
       
