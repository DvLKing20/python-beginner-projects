import time
import sys
CONTINUE = "'Yes' to Start or 'exit' to Exit"
SCORE = 1000
def ACTUAL_LOGIC(MORE_QUESTIONS,ANSWER,REAL_QUESTIONS):
 print(f"\n{REAL_QUESTIONS} : ")
 for i, FORMATTED in enumerate(MORE_QUESTIONS):
     if i % 2 == 0:
        sys.stdout.write(f"{FORMATTED + ': '}")   
     else:
        sys.stdout.write(f"{''.join(FORMATTED)}")
        if i == 3:
            print()
        if i == 1: 
            sys.stdout.write("    ")
        if i == 5:
                sys.stdout.write("   ")
        if i == 7:
            print()
                    
#  print(f"{REAL_QUESTIONS}\n {':  '.join(MORE_QUESTIONS[0:4])} \n { ': '.join(MORE_QUESTIONS[4:])}")

 global SCORE
 while True:
  User_Input = input("\nEnter The Alphabet Correspoding the Questuions : ").upper()
  
  if User_Input == ANSWER:       
       SCORE = SCORE * 2
       print("\nprocessing...")
       time.sleep(1)
       print("Congrats You Have Common Knowledge Twin :)")
       print(f"YOUR SCORE : {SCORE}")
       break
  else:
       print("\nprocessing...")
       time.sleep(1)
       print("Learn more Twin Tis a Wrong Answer Twin :)")
       print(f"YOUR SCORE : {SCORE}")
       print("\nYou Can Try Again From Starting\n")
       global NEXT
       NEXT = 'yes'
       break
NEXT = 'yes' 
while True:
       try:
        USER_INPUT = input(f"\n{CONTINUE} : ").lower()
        if USER_INPUT == 'exit':
           print("exiting...")
           time.sleep(1)
           print(f"YOUR SCORE : {SCORE}")
           break
       except ValueError:
           continue   
       if NEXT == 'yes':
            CONTINUE = 'Continue To Next Question'
            ABOUT = 'Which Scientist Developed The Theory of General Relativity'
            QUESTION_1 = ['A', 'Einstein', 'B', 'Nikola Tesla',
                          'C', 'Niel Bohr','D', 'None Of the Above']
            ANSWER = 'A'
            NEXT = USER_INPUT + '1'
            ACTUAL_LOGIC(QUESTION_1,ANSWER,ABOUT)

       elif NEXT == 'yes1':
            ABOUT = 'Why is Water Essential for Human Survival'
            QUESTION_1 = ['A', 'Hydration of cells', 'B', 'Removes Waste',
                          'C', 'Supports Digestion','D', 'All of the Above']
            ANSWER = 'D'
            NEXT = USER_INPUT + '2'
            ACTUAL_LOGIC(QUESTION_1,ANSWER,ABOUT)     
       elif NEXT == 'yes2':
            ABOUT = 'Who Invented Algebra'
            QUESTION_1 = ['A', 'AL-Khwarizmi', 'B', 'Avicenna',
                          'C', 'Mahatma Ghandi','D', 'None Of the Above']
            ANSWER = 'A'
            NEXT = USER_INPUT + '3'
            ACTUAL_LOGIC(QUESTION_1,ANSWER,ABOUT)
       elif NEXT == 'yes3':
            ABOUT = 'Who Formulated The Law of Universal Gravitation'
            QUESTION_1 = ['A', 'Isaac Newton', 'B', 'Thomas Eddison',
                          'C', 'Alan turing','D', 'All Of the Above']
            ANSWER = 'A'
            NEXT = USER_INPUT + '4'
            ACTUAL_LOGIC(QUESTION_1,ANSWER,ABOUT)
       elif NEXT == 'yes4':
            ABOUT = 'What Did Did Alexandar Fleming Discover'
            QUESTION_1 = ['A', 'DNA', 'B', 'Penicillin',
                          'C', 'Insulin','D', 'Germ theory']
            ANSWER = 'B'
            NEXT = USER_INPUT + '5'
            ACTUAL_LOGIC(QUESTION_1,ANSWER,ABOUT)
       elif NEXT == 'yes5':
            CONTINUE = "YOU HAVE COMPLETED THE CHALLENGE ENTER 'yes' TO CHECK YOUR SCORE"
            ABOUT = "If a Planet is Twice as far from the sun, according to Newton's Law of Gravitation, The Gravitational Force Becomes"
            QUESTION_1 = ['A', '2 Times Weaker', 'B', '4 Times Weaker',
                          'C', '8 Times Weaker','D', 'The Same']
            ANSWER = 'B'
            NEXT = USER_INPUT + '6'
            ACTUAL_LOGIC(QUESTION_1,ANSWER,ABOUT)                  
       elif NEXT == 'yes6':
            print("\n**CONGRAJULATIONS FOR COMPLETING THE CHALLENGE TWIN**")
            print(f"TWIN YOUR SCORE IS : {SCORE}")
            print("exiting...")
            time.sleep(1)
            break           
       else:
            print("Oops! You Entered Wrong Thing Try again : ")
            continue
          
     