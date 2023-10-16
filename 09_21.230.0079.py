print("Latihan")
a1 = "Diantara 6 sampai 10"
a2 = "Kurang dari sama dengan 6 atau lebih dari sama dengan 10"
a3 = "bukan angka 6 atau 10"
a4 = "Angka 6 atau 10"
s1 = True
s2 = not s1

gg = input("Masukan angka bebas : ")

print()
if (float(gg) >= 6 and float(gg) <= 10):
    print(a1, f"? {s1}")
else:
    print(a1, f"? {s2}")

print()
if (float(gg) <= 6 or float(gg) >= 10):
    print(a2, f"? {s1}")
else:
    print(a2, f"? {s2}")

print()
if (float(gg) == 6 or float(gg) == 10):
    print(a3, f"? {s2}")
else:
    print(a3, f"? {s1}")

print()
if (float(gg) == 6 or float(gg) == 10):
    print(a4, f"? {s1}")
else:
    print(a4, f"? {s2}")
