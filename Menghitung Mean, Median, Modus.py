#MENGHITUNG MEAN, MEDIAN, MODUS 

from functools import reduce
class Statistik: 
    def rataRata(self, x):
        total = reduce(lambda a,b: a + b, x)
        return total / len(x)
    
    def nilaiTengah (self, x):
        x.sort()
        if len (x) % 2 != 0:
            iTengah = [int(len(x)/2)]
        else: 
            iTengah = [int(len(x)/2) -1, int(len(x)/2)]
        aTengah = list(map(lambda a: x[a], iTengah)) #a = iTengah
        total = reduce(lambda x, y: x + y, aTengah)
        return total / len(aTengah)
    def modus (self, x): 
        x.sort()
        y = list(set(x))
        outPut = list(map(lambda a : x.count(a), y))
        angkaBanyak = max(outPut)
        indexAngkaBanyak = outPut.index(angkaBanyak)
        modus = y[indexAngkaBanyak]
        return modus

stat = Statistik()
print(stat.nilaiTengah([1, 2, 3, 4]))
print(stat.modus([1,2 ,3 ,4, 4, 4]))