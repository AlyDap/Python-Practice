# Integer ke Float
DT = 5
print(f"Tipe DT : {type(DT)} ,yakni {DT}\n")
# data ini akan diubah menjadi float
DF = float(DT)
print(f"Tipe DF menjadi {type(DF)} .Jadi {DF} \n")

# Float ke Int
DF = 10.9  # pembulatan ke bawah
print(f"tipe data DF {type(DF)} dengan nilai = {DF}\n")
# DF akan diubah manjadi int
DT = int(DF)
print(f"tipe data DT {type(DT)} dengan nilai = {DT}\n")


# Int ke String
DT = 4
print(f"tipe data DT {type(DT)} dengan nilai = {DT}\n")
# DT akan menjadi string
DS = str(DT)
print(f"tipe data DS sekarang {type(DS)} dengan nilai = {DS}\n")
# string tidak bisa di jumlah kali bagi dgn tipe int floaat
# N=1+DS

# Int ke numeric
ds = "22"  # bisa jika angka dan harus bil. bulat
di = int(ds)
df = (int(ds))
to = di+df
print(f"total dari {di}+{df}={to}\n")

# int ke bool
di = 1
db = bool(di)  # true
print(f"tipe data bool {type(db)} dengan nilai = {db}\n")
di = 0
db = bool(di)  # false
print(f"tipe data bool {type(db)} dengan nilai = {db}\n")
