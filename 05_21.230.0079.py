# operasi aritmatia */+-
q = 1
w = 1.5
h = q+w
print(f"{q}+{w}={h}")
h = q-w
print(f"{q}-{w}={h}")
h = q*w
print(f"{q}-{w}={h}")
h = q/w
print(f"{q}-{w}={h}")

# pangkat/eksponen**, modulus sisa bagi%
z = 4
x = 3
h = z**x
print(f"{z} pangkat {x} = {h}")
h = z % x
print(f"{z} dibagi {x} menghasilkan sisa bagi {h}")

# floor division // desimal hilang
a = 11
s = 4
h = a/s
print(f"{a} / {s} = {h}")  # menghasilkan angka desimal
h = a//s
print(f"{a} // {s} = {h}/n")  # menghasilkan angka desimal, dan pembulatan

# prioritas operasi
x = 3 - 4 + 5 * 6 / (3 + (11 - 4))
print(f"nilai dari x adalah {x} \n")
print('''diperoleh dari:
1. x = 3 - 4 + 5 * 6 / (3 + 7)
2. x = 3 - 4 + 5 * 6 / 10
3. x = 3 - 4 + 30 / 10
3. x = 3 - 4 + 3
4. x =-1 + 3
5. x = 2
''')

x = 4 + 5 * 2  # kali akan dihitung terlebih dahulu
y = (4 + 5) * 2  # dalam kurung akan dihitung terlebih dahulu
print(f"hasil x = {x} \n")
print(f"hasil y = {y}")
