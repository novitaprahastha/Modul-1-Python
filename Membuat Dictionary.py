#MEMBUAT DICTIONARY DAYS
days = { 
    'senin' : 'monday', 'selasa' : 'tuesday', 'rabu' : 'wednesday', 'kamis' : 'thursday', 
    'jumat' : 'friday', 'sabtu' : 'saturday', 'minggu' : 'sunday' }

#id = eng/ eng = id

hari = input('Ketik nama hari : ')
print(f'{hari.lower()} = {days.get(hari.lower(), )}')
print(f'{hari.upper()} = {days.get(hari.lower(), "Ga ada!")}')
print(f'{hari.upper()} = {days.get(hari.lower(), )}')
print(f'{hari.upper()} = {days.items(hari.lower(), "Ga ada!")}')