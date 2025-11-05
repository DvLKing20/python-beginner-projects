#made a class to Store book inside a single instance variable
import time
class Library:

    def __init__(self):
        self.THE_SHELF = ["HARRY POTTER", "ONCE UPON A TIME"]
        self.ADD_THE_STORY = ["THIS IS A STORY OF A MAGICIAN", "THERE ONCE LIVED A PRINCE"]
        
    def ADD_BOOKS(self):
            BOOK_NAME = input("ENTER THE BOOK NAME : ")
            STORY = input("ENTER THE STORY : ")
            print("\nADDING...")
            time.sleep(0.5)
            self.THE_SHELF.append(BOOK_NAME)
            self.ADD_THE_STORY.append(STORY)
            print("THE BOOK WAS ADDED SUCCESSFULLY CHECK ON DISPLAY TAB")

    def DISPLAY_BOOKS(self):
        for INDEX,BOOK in enumerate(self.THE_SHELF):
            print(f"{INDEX+1}: {BOOK}")
    
    def READ_BOOKS(self):
        USER_CHOOSEN_BOOK= int(input("ENTER THE BOOK INDEX : ")) - 1
        print(f"\n{self.ADD_THE_STORY[USER_CHOOSEN_BOOK]}")

REFERENCE_POINT = Library()
print("WELCOME TO THE LIBRARY")
while True:
   try:
      print("\n1: ADD A BOOK\n2: DISPLAY BOOKS\n3: READ BOOK")
      USER_INPUT = int(input("ENTER IT HERE : "))
      print()
   except  ValueError:
         print("\nERROR THATS NOT A NUMBER")
         continue
   
   if USER_INPUT == 1:
     REFERENCE_POINT.ADD_BOOKS()
   elif USER_INPUT == 2:
       REFERENCE_POINT.DISPLAY_BOOKS()
   elif USER_INPUT ==  3:
        REFERENCE_POINT.READ_BOOKS()
   else:
     print("\nTHAT OPERATION DOESNT EXIST")