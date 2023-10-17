# Dictionary
# list/array untuk mengakses data menggunakan indeks. Sedang dictionary mengakses data dengan identifier (key)
d={
 'key1':'value1',
 'key2':'value2',
 'keyN':'valueN',
}
print(type(d))
m={
 '01':'ali',
 '02':'aaaaali',
 '01':'ALI',
 '05':'ssss'
}
print(m)
print(m['01'],'\n')

# Operator Dictionary
# Panjang Dictionary
m={
 '01':'ali',
 '02':'aaaaali',
 '01':'ALI',
 '05':'ssss'
}
p=len(m)
print(f'Panjang list :{p}\n')

# Check key di Dictionary
m={
 '01':'ali',
 '02':'aaaaali',
 '01':'ALI',
 '05':'ssss'
}
k='02'
c=k in m
print(c)
k='1'
c=k in m
print(c,'\n')

# Akses data Dictionary 
m={
 '01':'ali',
 '02':'aaaaali',
 '01':'ALI',
 '05':'ssss'
}
print(m['01'])
# atau dapat dilakukan dengan perintah get. get dapat digunakan untuk membedakan bahwa yang kita akses adalah dictionary
print(m.get('01'))
print(m.get('11'))
print(m.get('11','data tidak ditemukan\n')) # dengan get kita bisa menambahkan string
# print(m['11']) #akan eror

# Update data dictionary
m={
 '01':'ali',
 '5':'ssss'
}
print(m)
m['5']='haha'
print(m,'\n')

# Delete dictionary
m={
 '01':'ali',
 '5':'ssss',
 'a': 2.3
}
del m['5']
print(m,'\n')
