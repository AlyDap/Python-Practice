import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,precision_score,recall_score, f1_score, classification_report


df=pd.read_excel('respon.xlsx','knn')
print(df)

print()
le = LabelEncoder()
print(f'field Jarak dari Pusat Kota SEBELUM dilakukan label encoder\n {df["Jarak_dari_Pusat_Kota"]}')

print()
df["Jarak_dari_Pusat_Kota"]=le.fit_transform(df["Jarak_dari_Pusat_Kota"])
df["Tingkat_Kepopuleran"]=le.fit_transform(df["Tingkat_Kepopuleran"])
df["Jenis_Tempat_Wisata"]=le.fit_transform(df["Jenis_Tempat_Wisata"])
print(f'field Jarak dari Pusat Kota SETELAH dilakukan label encoder\n {df["Jarak_dari_Pusat_Kota"]}')
print()
print(f'SEMUA field SETELAH dilakukan label encoder\n {df}')

# X kapital bukan class label (bukan Jenis_Tempat_Wisata)
X = df.iloc[:,0:2].values
Y = df.iloc[:,2:3].values
print('\n',X)
print('\n',Y)

X_train, X_test, y_train, y_test=train_test_split(X,df['Jenis_Tempat_Wisata'],test_size=0.2,random_state=10)

klasifikasi=MultinomialNB().fit(X_train,y_train)
prediksi = klasifikasi.predict(X_test)


print('\n',f'Tingkat akurasi : ', accuracy_score(y_test,prediksi))
print()

print(classification_report(y_test,prediksi,zero_division=0))
print()
# 2 1 0
# 2 taman, 1 pantai, 0 gunung

wisata=[[5, 7]]
prediksi=klasifikasi.predict(wisata)
prediksi_proba=klasifikasi.predict_proba(wisata)
print(f'Hasil prediksi proba wisata: ',prediksi_proba)
print()

for cari in prediksi:
    if cari==2:
        print('Hasil prediksi wisata = TAMAN')
    elif cari==1:
        print('Hasil prediksi wisata = PANTAI')
    else:
        print('Hasil prediksi wisata = GUNUNG')

print()
print(f'Hasil prediksi wisata: ',prediksi)
print()