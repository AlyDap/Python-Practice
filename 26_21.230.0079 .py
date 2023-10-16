# LATIHAN
# Buatlah list yang dapat menampung data inputan dari pengguna.
# list merupkan buku yang terdiri dari judul, pengarang, tahun
# contoh di bawah ini masih kurang tepat, belum bisa menambah data.

ali=0
data_buku=[]
data_buku1=[]
while True:

 print('Input Data Buku')

 judul = input('Judul buku :')
 pengarang = input('Nama Pengarang :')
 tahun = input('Tahun Terbit :')
 buku = [judul, pengarang, tahun]

 print('\n',buku)
 jawab=input('ketik dat lagi = ? (y/n)')

 data_buku.append(buku)
 data_buku1.extend(buku)
 if jawab=="n":
  break
 if jawab!='y':
  print('input salah bubarrr')
  break
   
# copy tidak bisa
# insert tidak bisa

print('\n','Data saat ini dengan append \n',data_buku)
print()
print('\n','Data saat ini dengan extend \n',data_buku1)