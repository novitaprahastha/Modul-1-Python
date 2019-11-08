#LAMBDA, MAP, FILTER AND REDUCE 

# nomor = [1 - 100]
# => amgka genap (filter)
# [2, 4, 6, 8,.....
# => setiap angka genap dikali 2 (map)
# [4, 8, 12, ......]
# => semua angka hasilnya dijumlahkan satu sama lain (reduce)
# [4 + 8 + 12+..........]

x = list(range(101))
#CARA 1: 
def angkaGenap (x): 
    if x % 2 == 0: 
        return True 
    else: 
        return False 
y = filter(angkaGenap, x)
# print(list(y))

z = list(map(lambda a: a * 2, x))
print(z)

from functools import reduce
c = reduce(lambda a, b : a + b, x)
print(c)
#=====================

#CARA 2:
z = reduce(lambda a, b : a + b, map(lambda a : a * 2, filter (lambda a : a % 2 == 0, x)))
print(z)