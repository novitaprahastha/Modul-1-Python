nama= 'Hari ini Hari tidak masuk sekolah'
# berapakah jumlah huruf h?

cari='h'
x=nama.upper().replace(cari.upper(), '')
print(x)
jmlcari=len(nama)-len(x)
print(f'Jumlah huruf\'{cari}\'ada={jmlcari}')

nama='Hari ini Hari tidak masuk sekolah karena hari Minggu'
#berapakah jumlah kata 'hari'? 
cari='hari'
x=nama.upper().replace(cari.upper(), '')
print(x)
jmlcari=int((len(nama)-len(x))/len(cari))
print(f'Jumlah kata\'{cari}\'ada={jmlcari}')
