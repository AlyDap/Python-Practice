#Perulangan

#For
#tampil huruf pada nama
nama="Aliii"
for huruf in nama: 
 print(huruf)
print("End 1")

#tampil angka pada range 5
for angka in range(5): 
 print(angka)
print("End 2")

#tampil angka dari pada range pertama - ke4 yakni 1,2,3
for angka in range(1,4): 
 print(angka)
print("End 3")

x=0
tot=0
himpunan = [0,8,5,6] # list, akan dijelaskan berikutnya
for i in himpunan:
 x += 1
 print(f'data ke {x} adalah {i}')
 tot += i
print('--------------------+')
print(f'total bilangan = {tot}')


#While
angka = 2
while angka >=-1:
 print(angka)
 angka-=1