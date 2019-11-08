#MEMBALIK KATA
kalimat = 'Hai aku Novita'
# 'iaH uka ativoN'

def reverse (s): 
    str = ''
    for i in s: 
        str = i + str
    return str
s = 'Hai Aku Novita Prahastha Dewi'
print('String awal :',  end = ' ')
print(s)
print ('String yang sudah di balik: ',  end = '')
print(reverse(s))