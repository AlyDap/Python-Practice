# Tipe Data List
# List adalah struktur data pada python yang mampu menyimpan lebih dari satu data, seperti array
kump_number = [1,2,4.5,6]
print(f'ini tipe data list yang berisi kumpulan angka :{kump_number}')
kump_string = ['joni','lala']
print(f'ini tipe data list yang berisi kumpulan huruf :{kump_string}')
campuran = [1,2,4.5,'rina']
print(f'ini tipe data list yang berisi campuran huruf & angka :{campuran}')
print()

# List dengan Range
data_range=range(0,5) # step range tambah 1
list_range=list(data_range)
print(f'ini tipe data list yang dibuat dengan range :{list_range}')
data_range=range(1,10,2) # step range tambah 2
list_range=list(data_range)
print(f'ini tipe data list yang dibuat dengan range :{list_range}')
print()

# List dengan For
list_for = [i for i in range(0,4)]
print(f'ini tipe data list yang dibuat dengan for :{list_for}')
list_for = [i**2 for i in range(0,4)]
print(f'ini tipe data list yang dibuat dengan for :{list_for}')
print()

# List dengan For dan If
list_for_if = [i for i in range(1,10) if i != 3] # 3 tidak masuk ke dalam range
print(list_for_if)
list_for_if = [i for i in range(1,10) if i % 2 == 0] # ditampilkan nilai yang punya modulus 0 saat dibagi 2
print(list_for_if)
list_for_if = [i for i in range(1,10) if i % 2 != 0] # ditampilkan nilai yang tidak punya modulus 0 saat dibagi 2
print(list_for_if)
print()

# Index pada list
data = ['ali','rina',34, 5.5]
print(f'indek ke 0 : {data[0]}')
print(f'indek ke 1 : {data[1]}')
print(f'indek ke 2 : {data[2]}')
print(f'indek ke 3 : {data[3]}\n')
print(f'indek ke -1 : {data[-1]}')
print(f'indek ke -2 : {data[-2]}')
print(f'indek ke -3 : {data[-3]}')
print(f'indek ke -4 : {data[-4]}')
print()