import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,precision_score,recall_score, f1_score, classification_report




# os.chdir("D:\\ALI_5P52\\pert1011")

nama_file='dataset_template_tugas.xlsx'
sheet_names='dataset'
daftar_sheet=pd.ExcelFile(nama_file).sheet_names

df = pd.read_excel(nama_file, sheet_name= sheet_names)
print(df)

print()
le = LabelEncoder()
print(f'field jurusan SEBELUM dilakukan label encoder\n {df["JURUSAN"]}')

print()
df["JURUSAN"]=le.fit_transform(df["JURUSAN"])
df["GENDER"]=le.fit_transform(df["GENDER"])
df["ASAL_SEKOLAH"]=le.fit_transform(df["ASAL_SEKOLAH"])
df["RERATA_SKS"]=le.fit_transform(df["RERATA_SKS"])
df["ASISTEN"]=le.fit_transform(df["ASISTEN"])
df["STUDY"]=le.fit_transform(df["STUDY"])
print(f'field jurusan SETELAH dilakukan label encoder\n {df["JURUSAN"]}')
print()
print(f'SEMUA field SETELAH dilakukan label encoder\n {df}')

# X kapiral bukan class label (bukan study)
X = df.iloc[:,0:5].values
Y = df.iloc[:,5:6].values
print('\n',X)
print('\n',Y)

X_train, X_test, y_train, y_test=train_test_split(X,df['STUDY'],test_size=0.2,random_state=10)

klasifikasi=MultinomialNB().fit(X_train,y_train)
prediksi = klasifikasi.predict(X_test)


print('\n',f'Tingkat akurasi : ', accuracy_score(y_test,prediksi))
print()

print(classification_report(y_test,prediksi,zero_division=0))
print()
# 2 0 0 1 0
# ips=2  ipa=1  bahasa=0
# ips=2  ipa=1  bahasa=0

jhoni=[[2, 0, 0, 1, 0]]
prediksi=klasifikasi.predict(jhoni)
prediksi_proba=klasifikasi.predict_proba(jhoni)
print(f'Hasil prediksi proba Jhoni: ',prediksi_proba)
print()

for cari in prediksi:
    if cari==0:
        print('Hasil prediksi Jhoni = tepat')
    else:
        print('Hasil prediksi Jhoni = terlambat')

print()
print(f'Hasil prediksi Jhoni: ',prediksi)
print()