import random
from word_tuple import WORDS

class hang_man_game:
    
    def __init__(self,WORDS):
        self.words = WORDS
        self.random_word = random.choice(self.words)
        self.hints = []
        self.hang_man_art = (("    ",
                              "    ",
                              "     "),
                             ("  O ",
                              "    ",
                              "     "),
                             ("  O ",
                              "  | ",
                              "    "),
                             ("  O  ",
                             r"  |\ ",
                              "      "),
                             ("  O  ",
                             r" /|\ ",
                              "      "),
                             ("  O  ",
                             r" /|\  ",
                              " /    "),
                            ("  O   ",
                           r" /|\  ",
                           r" / \  "))
        
    def show_hint(self):
         for _ in range(len(self.random_word)):
                self.hints.append("_")

    def show_alpha(self,i):
        print()
        print("-------------------------------------")
        user_answer = input("Enter your answer!: ").lower()
        if user_answer in self.random_word:
           for index, word in enumerate(self.random_word):
               if user_answer == word:
                   self.hints[index] = word 
               else:
                 continue
           return 0 
        else:
            for art in self.hang_man_art[i]:
                print(art)
            return 1

    def main(self):
        self.show_hint()
        i = 0
        while "_" in self.hints:
          if i > 6:
              print("You lost")
              break
          print(''.join(self.hints))
          i += self.show_alpha(i)
        else:
            print("You Won")

if __name__ == "__main__":
 REF = hang_man_game(WORDS)
 REF.main()