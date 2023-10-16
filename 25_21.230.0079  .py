# Looping List dan Enumerate
# untuk menampilkan atau mengakses data pada list kita dapat menggunakan looping dan enumerate

# Looping
data = ['Ali','rika','slamet','bejo']

# menggunakan for
for n in data:
 print(n)
print('---- end for ---- \n')

# menggunakan konsep for pada pemrograman lain
pd= len(data)
for n in range(pd):
 print('nama:',data[n])
print('---- end for ---- \n')

# menggunakan while
i=0
while i<pd:
 print(f'nama: {data[i]}')
 i+=1
print('---- end while ---- \n')

# List Comprehension
data = ['Ali','rika','slamet','bejo']
cetak=[print(f'nama :{i}') for i in data]
print()
cetak=[print(f'nama:{a}') for a in data]
print()

# Enumerate
print('----- ENUMERATE -----')
data = ['Ali','rika','slamet','bejo']
for index,data in enumerate(data):
 print(f'index = {index}, data = {data}')
 for index, data in enumerate(data):
  print(f'index={index}, data={data}')
 print()