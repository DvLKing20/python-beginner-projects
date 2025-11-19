import random
import string

class Encode_Decode:
    def __init__(self):
        self.ran_dict = {}
        self.ran_chars = " "+string.punctuation + string.ascii_letters 
        self.ran_chars = list(self.ran_chars)
        self.copy_ran_chars = self.ran_chars.copy()
        random.shuffle(self.copy_ran_chars)

    def ancient_encryption(self):
        user_stuff = input("Enter The Stuff You Want to Encrypt: ")
        for stuff in user_stuff:
          while True:
              value = random.choice(self.copy_ran_chars)
              if value not in self.ran_dict:
                 self.ran_dict[value] = stuff
                 break
              else:
                  continue

    def show(self):
        for keys in self.ran_dict.keys():
              print(keys,end="")

    def ancient_decryption(self):
        user_keys = input("Enter The Keys to Decode :")
        for key in user_keys:
           real_char = self.ran_dict.get(key)
           if real_char:
               print(real_char,end="")
           else:
               pass
               







if __name__ == "__main__":      
 reference = Encode_Decode()
 reference.ancient_encryption()
 reference.show()
 print()
 reference.ancient_decryption()