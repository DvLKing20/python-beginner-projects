s = 'this a sexy moon   '
i = len(s) - 1
count = 0

# while i >= 0 and s[i] == ' ':
#     i -= 1

# while i >= 0 and s[i] != ' ':
#     count +=1
#     i-= 1

# print(f"{count}")   
def AnotherTry(s,i,count):
    for i in range(len(s)-1,-1,-1) :
        if i >= 0 and s[i] == ' ':
            print(f"{i}")
        elif i >= 0 and s[i] != ' ':
            count += 1
            print(f"{i}")
    print(f"{count}")            
AnotherTry(s,i,count)   