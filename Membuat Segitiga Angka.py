#MEMBUAT SEGITIGA ANGKA 

def angkaSegitiga1 (x): 
    angka = ''
    for i in range (x): 
        for j in range (i): 
            print(j + 1, end = ' ')
        print()
angkaSegitiga1(6)

def angkaSegitiga2 (x): 
    angka = ''
    for i in range (x): 
        for j in range (0, x - i): 
            print(j + 1, end = ' ')
        print()
angkaSegitiga2 (5)

def angkaSegitiga3 (x): 
    angka = ' '
    for i in range (x): 
        print(str(i)*i, end = '')
        print()
angkaSegitiga3 (6)
