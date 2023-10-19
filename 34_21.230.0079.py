# Latihan
# membuat header
import os

end = 1
while (end <= 2):
    os.system("cls")

    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILITNG PERSEGI PANJANG':^40}")
    print(f"{'_'*40:^40}")

    # membuat input
    LEBAR = int(input("Nilai Lebar :"))
    PANJANG = int(input("Nilai Panjang :"))

    # program hitung
    LUAS = PANJANG*LEBAR
    KELILING = 2*(PANJANG+LEBAR)

    # tampilkan hasil
    print(f"\nHasil Luas = {LUAS}")
    print(f"Hasil Keliling = {KELILING}")

    while (end < 2):
        cek = input("Input lagi? [Y/T] :")
        if (cek == 'y' or cek == 'Y'):
            break
        elif (cek == 't' or cek == 'T'):
            end = 3
        else:
            end = 1
