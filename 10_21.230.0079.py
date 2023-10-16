#Operator Assigment
a = 4
a += 1 # a = a + 1, --> a = 4 + 1
print(f"nilai a = 4, a += 1 hasilnya {a}\n")

a = 4
a -= 1 # a = a - 1, --> a = 4 - 1
print(f"nilai a = 4, a -= 1 hasilnya {a}\n")

a = 4
a *= 2 # a = a * 2, --> a = 4 * 2
print(f"nilai a = 4, a *= 2 hasilnya {a}\n")

a = 4
a **= 2 # a = a ** 2, --> a = 4 ** 2
print(f"nilai a = 4, a **= 2 hasilnya {a}\n")

a = 4
a /= 2 # a = a / 2, --> a = 4 / 2
print(f"nilai a = 4, a /= 2 hasilnya {a}\n")

a = 3
a %= 2 # a = a % 2, --> a = 4 % 2
print(f"nilai a = 3, a %= 2 hasilnya {a}\n")

a = 3
a //= 2 # a = a // 2, --> a = 4 // 2
print(f"nilai a = 3, a //= 2 hasilnya {a}\n")

a = 0b11011
print(f"nilai a = {a}, dengan format bit:\t\t {format(a,'08b')}")
a >>= 1
print(f"nilai a = {a}, a >>= 1, format bit menjadi:\t {format(a,'08b')}")
a <<= 1
print(f"nilai a = {a}, a <<= 1, format bit menjadi:\t {format(a,'08b')}")