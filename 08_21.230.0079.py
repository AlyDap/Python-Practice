# Operator Logika
# Not
e = True
ee = not e
print("NOT kebalikan")
print(ee, "\n")

# And
print("AND")
e = True
ee = False
eee = e and ee
print(f"hasil dari {e} and {ee} = {eee}")
e = True
ee = True
print(f"hasil dari {e} and {ee} = {e and ee}")
e = False
ee = False
print(f"hasil dari {e} and {ee} = {e and ee}\n")

# Or
print("OR")
e = True
ee = False
eee = e or ee
print(f"hasil dari {e} or {ee} = {eee}")
e = True
ee = True
print(f"hasil dari {e} or {ee} = {e or ee}")
e = False
ee = False
print(f"hasil dari {e} or {ee} = {e or ee}\n")

# Xor
print("XOR akan true jika salah satu true, selain itu false")
e = True
ee = False
eee = e ^ ee
print(f"hasil dari {e} xor {ee} = {eee}")
e = True
ee = True
print(f"hasil dari {e} xor {ee} = {e ^ ee}")
e = False
ee = False
print(f"hasil dari {e} xor {ee} = {e ^ ee}\n")
