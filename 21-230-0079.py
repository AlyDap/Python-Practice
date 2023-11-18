# Latihan
# membuat header
import os
import matplotlib.pyplot as grafik
# import numpy as np



data1=[]
data2=[]
end = 1
while (end <= 2):
    # os.system("cls")

    # membuat input
    nama = input("Masukan Nama : ")
    nilai = int(input("Nilai : "))
    
    tambah=data1.append(nama)
    tambah2=data2.append(nilai)



    while (end < 2):
        cek = input("Input lagi? [Y/N] :")
        if (cek == 'y' or cek == 'Y'):
            os.system("cls")
            print('Data Saat Ini')
            # print(f"List Data Nama : {nama}")
            print(f"List Data Nama : {data1}")
            print(f"List Data Nilai : {data2}")
            print()
            break
        elif (cek == 'n' or cek == 'N'):
            os.system("cls")
            print('Data Saat Ini')
            # print(f"List Data Nama : {nama}")
            print(f"List Data Nama : {data1}")
            print(f"List Data Nilai : {data2}")
            print()
            end = 3
        else:
            end = 1
            
# print(tambah)
# print(tambah2)
# x=['A','B','C','D','E']
# y=[3,5,2,4,1]
fig, ax =grafik.subplots()
ax.plot(data1, data2)
grafik.show()
