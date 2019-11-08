#MENGHITUNG INDEX HARI 

hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
# "Sekarang hari 'Rabu', hari apakah 100 hari lagi?"

now = 'rabu' ; brphari = 100
iNow = hari.index(now) 
print(iNow)
sisahari = brphari % len(hari)
hariyangdicari = hari[(iNow + sisahari) % 7]
print(hariyangdicari)