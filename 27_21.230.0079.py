# Tuples dan Set
# Tuples 
# Tuple adalah jenis dari list yang tidak dapat diubah elemennya. Umumnya tuple digunakan untuk data yang bersifat sekali tulis, dan dapat
# dieksekusi lebih cepat. Tuple didefinisikan dengan kurung dan elemen yang dipisahkan dengan koma

d=(1,2,22,31,53,21,2,5,7,3)
print(d[0])
print(d)
# d[0]=4 error
print()

# Cara Nulis Tuples
# Untuk membuat tuples, kata tidak harus diawali dan diakhiri dengan tanda kurung
 
d=1,2,3 #tuples
print(d)
print(type(d))

n=(1) # jika datanya cuma satu, tidak disebut sebagai tuples
print(n)
print(type(n))

a=1 #bukan tuples
print(a)
print(type(a))
print()

# Join Tuples
d1=1,2,3
d2='ali','ALI'
g=d1+d2
print(g,'\n')

# List ke Tuple
d=['ALI','ali',1,2]
print(d)
print(type(d))
dd=tuple(d)
print(dd)
print(type(dd))

# Set
# Set adalah kumpulan item bersifat unik dan tanpa urutan (unordered collection). Didefinisikan dengan kurawal dan elemennya dipisahkan dengan
# koma. Karena set bersifat unordered, maka kita tidak bisa mengambil sebagian data / elemen datanya menggunakan proses slicing
d={1,2,'ali'}
print('\n',d)
print(type(d),'\n')
# print('\n',d[0]) error

# Add item ke Set
d={1,1,1,1,2,}
print(d)
d.add('ali')
print(d)
for d in d:
 print(d,'\n')

# merge SET
d1={1,1,1,3}
d2={3,1,23,5,5}
dd=d1.union(d2)
print(dd)
print(type(dd),'\n')

# Add data antar Set
d1={1,1,2}
d2={'ali','ALI','ALI'}
d1.update(d2)
print(d1,'\n')

# Delete item Set
d1={'ali','ali','Ali','1',1,1,2,2,3}
d1.remove('ali')
d1.remove(1)
print(d1,'\n')

# Delete Set
d2={1,2}
del d2
# print(d2) error karena data sudah dihapus