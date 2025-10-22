# num = [7,2,5,1]
# target = 9
# def __init__(num,target):
#     for i in range(len(num)):
#         for j in range(i+1, len(num)) :
#             if num[i] + num[j] == target:
#                 return (i,j)
            
# Result = __init__(num,target)
# print(f"The Following Result : {Result}")

s = 'Niggas lover '

def slicing(s):
    count = 0 
    i = len(s) -1
    for i in range(len(s) -1,-1,-1):
        if s[i] == ' ':
            i -= 1
        else:
            count += 1
        
        # if i >= 0 and s[i] != ' ':
        #     count = count + 1
        # elif s[i] == ' ':
        #         return count
                 
result = slicing(s)
print(f"{result}")