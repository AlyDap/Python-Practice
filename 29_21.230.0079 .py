# Looping Dictionary
m={
 '1':'A',
 '2':'S',
 '3':'D',
 '4':'W',
}
print('--- Ambil Keys saja ---')
for nama in m :# cara ini hanya akan menampilkan keys nya aja..
 print(nama)

print()
print('--- Ambil data berdasarkan keys ---')
key=m.keys() # untuk menampilkan datanya, maka kita perlu mendekalarasikan keysnya
for nama in key:
 print(m.get(nama))

print()
print('--- Ambil data berdasarkan values ---')
value=m.values() # untuk menampilkan datanya, maka kita perlu mendekalarasikan valuesnya
for nama in value:
 print(nama)

print()
print('--- Ambil semua item pd dictionary ---')
semua=m.items() # akan nemampilkan semua data dalam bentuk tuple
for nama in semua:
 print(nama)

print()
print('--- Ambil data dr semua item pd disctionary ---')
for key,nama in semua:
 print(f'key : {key}, nama : {nama}') #akan nemampilkan semua item pada Dictionary