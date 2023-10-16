#Operator Method String
#count() menghitung jumlah huruf
n="Muhammad Ferdynan Ali Syahbana"
h="A"
sum=n.count(h)
print(f"jumlah huruf {h} pada nama {n} :",sum)
print()

#upper() mengubah huruf kecil menjadi hurus Kapital
#lower() mengubah huruf kapital menjadi hurus kecil
k="Sinau Python"
print(f"kalimat awal = {k}, setelah di upper = {k.upper()}")
print(f"kalimat awal = {k}, setelah di lowwer = {k.lower()}")
print("~~"*11,"Pengecekan Lower Upper","~~"*11)
k="hi"
print(f"Apa kata {k} kecil semua? {k.islower()}")
print(f"Apa kata {k} kapital semua? {k.isupper()}")
print()

#istitle() mengecek apakah semua kata diawali dengan huruf kapital
j="Sinau Python"
print('apa judul "',(j),'"',"setiap katanya diawali huruf kapital? ",(j.istitle()))
print()

#startswitch()  melakukan pengecekan kata di awal kalimat
#endswitch() melakukan pengecekan kata di akhir kalimat
kalimat = "Ali sinau python"
kata_depan = "Ali"
print(f'kalimat "{kalimat}" memiliki kata depan "{kata_depan}", jawab: {kalimat.startswith(kata_depan)}')
kata_akhir = "Python"
print(f'kalimat "{kalimat}" memiliki kata depan "{kata_akhir}", jawab: {kalimat.endswith(kata_akhir)}')
print()

# "rjust()" alokasi karakter untuk ke kanan
# "ljust()" alokasi karakter untuk ke kiri
# "center()" alokasi karakter untuk ke tengah
kata = "1234567"
kanan = kata.rjust(10) # menempaktan kata 1234567 ke kanan pada posisi 10
kiri = kata.ljust(10) # menempaktan kata 1234567 ke kiri pada posisi 10
tengah = kata.center(10) # menempaktan kata 1234567 ke tengah di posisi 10
print("'",kanan)
print(kiri,"'")
print("'",tengah,"'\n")
# menempaktan kata 1234567 ke kanan pada posisi tertentu dan menambahkan karakter
kanan = kata.rjust(10,'-')
kiri = kata.ljust(10,'-')
tengah = kata.center(10,'-')
print("'",kanan)
print(kiri,"'")
print("'",tengah,"'")
print("###"*7)

#strip() menghilangkan karakter
kata = "1234567"
kanan = kata.rjust(10,'-')
kiri = kata.ljust(10,'-')
tengah = kata.center(10,'-')
print("'",kanan)
print(kiri,"'")
print("'",tengah,"'\n")
# setelah di strip()
kanan = kata.strip('-')
kiri = kata.strip('-')
tengah = kata.strip('-')
print("'",kanan)
print(kiri,"'")
print("'",tengah,"'")
print("###"*7)

#isalpha() mengecek apakah semuanya berupa huruf
kata = "python"
cek = kata.isalpha()
print(f'apakah "{kata}" semuanya huruf, jawab: {cek}\n')
kata = "12 python"
cek = kata.isalpha()
print(f'apakah "{kata}" semuanya huruf, jawab: {cek}')

#isalnum() =>mengecek kata apakah terdiri dari kombinasi angka dan huruf
kata = "12 python"
cek = kata.isalnum()
print(f'apakah "{kata}" semuanya huruf, jawab: {cek}')

#isdecimal() mengecek apakah terdiri dari angka semua
kata = "12345" #kata bertipe data string yang isinya 12345, dalam hal ini bukan numeric
cek = kata.isdecimal()
print(f'apakah "{kata}" semuanya angka, jawab: {cek}')

# isspace() mengecek spasi, tab, newline
kalimat = "Saya belajar python"
cek = kalimat.isspace()
print(f'apakah kalimat "{kalimat}" merupakan spasi, jawab: {cek}')
kalimat = " "
cek = kalimat.isspace()
print(f'apakah kalimat "{kalimat}" merupakan spasi, jawab: {cek}')
kalimat = "\t \n"
cek = kalimat.isspace()
print(cek)