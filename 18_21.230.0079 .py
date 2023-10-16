#Latihan
n1=input("Masukan Angka pertama : ")
p=input("Pilih Operator \n\t1  + Penjumlahan\n\t2  - Pengurangan\n\t3  * Perkalian\n\t4  / Pembagian\n\t5  % Sisabagi\n\t\t Pilih [1-5] :")
n2=input("Masukan Angka kedua : ")
if p=="1":
 n3="+"
 nn=int(n1)+int(n2)
elif p=="2" :
 n3="-"
 nn=int(n1)-int(n2)
elif p=="3" :
 n3="*"
 nn=int(n1)*int(n2)
elif p=="4" :
 n3="/"
 nn=int(n1)/int(n2)
elif p=="5" :
 n3="%"
 nn=int(n1)%int(n2)
else : print("Input Pilihan tidak benar")
if (p=="1" or p=="2" or p=="3" or p=="4" or p=="5"):
# if p== ("1" or "2" or "3" or "4" or "5")  : tidak bisa
 print ("Hasil",n1,n3,n2,":",nn)