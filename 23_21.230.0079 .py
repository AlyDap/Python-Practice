# Operasi List #1
# Len 
# Mencari jumlah data pada list
data = ['ali','rina',34, 5.5]
print(f'jumlah data pada list data : {len(data)}')
print()

# Menambah data List
# Insert
# Menambah item pada posisi tertentu
data = ['ali','rina',34, 5.5]
print(f'data sebelum ditambah : {data}')
tambah = data.insert(0,'joni') # menambahkan joni pada posisi indeks ke nol pada lis data
print(f'setelah ditambah menjadi : {data}')
print()

# Append
# Menambah item pada posisi terakhir
data = ['ali','rina',34, 5.5]
print(f'data sebelum ditambah : {data}')
tambah = data.append('joni') # menambahkan joni pada posisi terakhir
print(f'setelah ditambah menjadi : {data}')
print()

# Extend = Merge List
data1 = ['ali', 'ali2', 'ali3']
data2 = ['ali', 'surya',5]
data1.extend(data2)
print(data1)
print()

# Mengubah Data
data1 = ['ali', 'ali2', 'ali3']
data1[0] = 'slamet'
print(data1)
print()

# Menghapus Data
data1 = ['ali', 'ali2', 'ali3']
data1.remove('ali') # menghapus data sesuai parameter yang dimasukkan
print(data1)
data1 = ['ali', 'ali2', 'ali3']
data1.pop() # menghapus data paling akhir
print(data1)
print()


# Count() Mencari jumlah data yang sama
data1 = ['ali', 'ali2', 'ali3',1,1,4,5,6,7,4,8,2,1,1,'ali']
jumlah_ali = data1.count('ali')
jumlah_1 = data1.count(1)
print(f'jumlah data ali ada "{jumlah_ali}"')
print(f'jumlah data 1 ada "{jumlah_1}"')
print()

# Mencari index Data
Data = ['rina','ali','lisa', 6.5, 7]
cari_index = Data.index('rina')
cari = Data[0]
print(f'rina ada di index ke {cari_index} pada list Data')
print(f'indek ke 0 adalah {cari}')
print()


# Sorting Data
# Tidak bisa digabungkan dengan string / int saat dishor
# sort() Ascending 
data = [1,5,2,3,8,5,90,4.5]
print(f'data sebelum di sorting : {data}')
data.sort()
print(f'data setelah di sorting : {data}\n')
data_str = ['zafira','xenia','vw','bmw','golden','ford','yolk','wagoon','kamal']
print(f'data sebelum di sorting : {data_str}')
data_str.sort()
print(f'data setelah di sorting a ke z: {data_str}')
print()


# reverse() Descending
data_angka = [1,5,2,3,80,4.5]
print(f'data sebelum di sorting : {data_angka}')
data_angka.sort(reverse=True)
print(f'data setelah di sorting large to small: {data_angka}')
print()
