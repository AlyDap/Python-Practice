# Copy Dictionary
# Copy 
s={
 '1':'Ali',
 '2':'Bagas',
 '3':'Cimoy',
}
std=s.copy()
print(f'Data siswa = {s}')
print('Data std =',std,'\n')

# Pop Dictionary
# Mengeluarkan data dari Dictionary ke varibel lain
# pop() maling data tertentu
s={
 '1':'Ali',
 '2':'Bagas',
 '3':'Cimoy',
}
print('Data awal :\t\t',s)
s2=s.pop('1')
print('Data yang diambil :\t',s2)
print('Data sesudah diambil :\t',s,'\n')

# popitm() mengambil data yang terakhir
s={
 '1':'Ali',
 '2':'Bagas',
 '3':'Cimoy',
}
print('Data awal :\t\t',s)
s2=s.popitem()
print('Data akhir yg diambil :\t',s2)
print('Data sesudah diambil :\t',s,'\n')

