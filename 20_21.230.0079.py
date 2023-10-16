#Countine Break Pass

#Pass  antara ada dan tiada
angka = 0
while angka <5:
 angka += 1
 if angka == 3:
  print(f'ini angka {3}')
 else:
  print(angka)
print(10*'-')

angka = 0
while angka <5:
 angka += 1
 if angka == 3:
  pass
 print(angka)
print(21*"_")
print()


#Continue  Membuat loop meloncat ke step berikutnya
angka = 5
while angka >=0:
 print(angka)
 angka -= 1
 if angka == 3:
  print('muncul')
print('-------------------')

angka = 5
while angka >=0:
 print(angka)
 angka -= 1
 if angka == 3:
  continue #karena ada continue perintah print diabaikan dan langsung melanjutkan perulangan
  print('hi tidak tampil')
  print('tidak muncul')
print(21*"_")
print()


#Break  memaksa perulangan berhenti sebelum waktunya
angka = 5
while angka >=0:
 print(angka)
 angka -= 1
 if angka == 3:
  print('muncul')
print('-------------------')
angka = 5
while angka >=0:
 print(angka)
 angka -= 1
 if angka == 3:
  break #karena ada break perulangan dihentikan
  print('muncul')
print('-------------------')


angka = int(input('Ngulang sampai :'))
awal = 0
while True:
 awal += 1
 print(awal)
 if awal==angka:
  break