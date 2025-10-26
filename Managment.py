import time
class Person:
    def __init__(self,name,age,Occupation):
        self.name = name
        self.age = age
        self.Occupation = Occupation
        self.task = None

    def greet(self):
      print(f"hi I am {self.name} my age is {self.age} and my occupation is {self.Occupation}")

    def ASSIGN_TASK(self,task):
        self.task = task
        print(f"{self.name} YOUR TASK IS {self.task}")


def CREATE_PERSON():  
      PERSON_NAME = input("Enter the Name : ")
      PERSON_AGE =  input("Enter the Age : ")
      PERSON_OCCUPATION = input("Enter the Occupation : ")
      return PERSON_NAME,PERSON_AGE,PERSON_OCCUPATION
   
PERSONS_LISTS = []
while True:
     print("\n1: RECRUIT\n2: CHECK RECRUITS\n3: ASSIGN TASK")
     MAKE_CHOICE = int(input("\nENTER HERE : "))
     if MAKE_CHOICE == 1:
        PERSON = Person(*CREATE_PERSON())
        PERSONS_LISTS.append(PERSON)
     elif MAKE_CHOICE == 2:
          i = 0
          for PERSON in PERSONS_LISTS:
              i+=1
              print(f"{i}: ",end="")
              PERSON.greet()
     elif MAKE_CHOICE == 3:
           if not PERSONS_LISTS:
             print("\nNO ONE TO ASSIGN THE TASK TO!")
             continue
           elif MAKE_CHOICE == 3:
               for INDEX,PERSON in enumerate(PERSONS_LISTS):
                   print(f"{INDEX+1}: {PERSON.name}")
               ASSIGN_TASK_TO = int(input("WHO TO ASSIGN TASK : ")) - 1
               ASSING_THE_TASK = input("WHAT TASK TO ASSING : ")
               PERSONS_LISTS[ASSIGN_TASK_TO].ASSIGN_TASK(ASSING_THE_TASK)
           elif MAKE_CHOICE == 0:
                print("\nEXITING...")
                time.sleep(1)
                break 
           else:
               print("\nERROR ENTER A VALID NUMBER")
               continue
               
           