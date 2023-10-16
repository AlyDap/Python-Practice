#Format String

#Generic
n="ALi"
f_str= f"hi {n}"
print(f_str)
nn=100
# f=f"{n} mendapat nilai {nn}. Nilai "+nn+" adalah nilai?"
#error karena int
f=f"{n} mendapat nilai {nn}. Nilai {nn} adalah nilai?"
print(f)

#Format bilangan ordo ribuan = bisa memformat uang
angka = 15000
format_str = f"angka = {angka:,}"
print(format_str)
angka = 15000000
format_str = f"angka = {angka:,}"
print(format_str)

#Format bil. decimal = menampilkan berapa angka di belakang titik
angka = 15.987665
format_str = f"angka = {angka:.3f}" 
print(format_str)

#Leading Zeros
angka = 15.987665
print(f"menampilkan angka decimal {angka}")
print(f"menampilkan angka decimal {angka:.3f}")
print(f"menampilkan angka decimal {angka:08.3f}") #leading zeros