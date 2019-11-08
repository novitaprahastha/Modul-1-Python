#PALINDROME
# ex: 
# katak = katak True
# malam = malam True 
#bantal != latnab False 

#CARA 1 :
x = 'malam'
y = ''.join(list(x[: : -1])) 
#==============================

#CARA 2:
def palindrome (kata): 
    if kata == kata[: : -1]:
        return True
    else: 
        return False
print(palindrome(x))
#===========================================

##CARA 3:
def palindrome2 (kata): 
    for i in range(round(len(kata)/2)): 
        palindromekah = False 
        if kata[i] == kata[len(kata)-1 - i]: 
            palindromekah = True 
        else: 
            palindromekah = False 
            break 
    return palindromekah
print(palindrome2('malam'))