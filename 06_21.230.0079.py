# Konversi Suhu
# Dari C ke K R F
#   K=C+273
#   R=4/5*C
#   F=9/5*C+32
# Dari K ke C R F
#   C = K – 273
#   R = 4/5 (K-273)
#   F = 9/5 (K-273) + 32
# Dari R ke C K F
#   C = (5/4) R
#   F = (9/4) R + 32
#   K = C + 273 = (5/4) R + 273
# Dari F ke C K R
#   C = 5/9 (F-32)
#   R = 4/9 (F-32)
#   K = 5/9 (F-32) + 273

print("Konversi Suhu Celcius Kelvin Reamur Fahrenheit")
I = input(
    "1 Dari Celcius \n2 Dari Kelvin \n3 Dari Reamur \n4 Dari Fahrenheit \n  Masukan angka[1-4] : ")

if (I == "1"):
    C = input("\nMasukan Celcius : ")
    K = float(C)+273
    R = 4/5*float(C)
    F = 9/5*float(C)+32
    print(f"Dari Celcius : {C}")
    print("Menjadi Kelvin :", K)
    print("Menjadi Reamur :", R)
    print("Menjadi Fahrenheit :", F)
    print(5*"_______")

elif (I == "2"):
    K = input("\nMasukan Kelvin : ")
    C = float(K)-273
    R = 4/5*(float(K)-273)
    F = 9/5*(float(K)-273)+32
    print(f"Dari Kelvin : {K}")
    print("Menjadi Celcius :", C)
    print("Menjadi Reamur :", R)
    print("Menjadi Fahrenheit :", F)
    print(5*"_______")

elif (I == "3"):
    R = input("\nMasukan Reamur : ")
    C = 5/4*float(R)
    K = 5/4*float(R)+273
    F = 9/4*float(R)+32
    print(f"Dari Reamur : {R}")
    print("Menjadi Celcius :", C)
    print("Menjadi Kelvin :", K)
    print("Menjadi Fahrenheit :", F)
    print(5*"_______")

elif (I == "4"):
    F = input("\nMasukan Fahrenheit : ")
    C = 5/9*(float(F)-32)
    R = 4/9*(float(F)-32)
    K = 5/9*(float(F)-32)+273
    print(f"Dari Fahrenheit : {F}")
    print("Menjadi Celcius :", C)
    print("Menjadi Reamur :", R)
    print("Menjadi Kelvin :", K)
    print(5*"_______")

else:
    print("BYE")
