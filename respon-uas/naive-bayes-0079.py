import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,precision_score,recall_score, f1_score, classification_report


df=pd.read_excel('respon.xlsx','nb')
print(df)

print()
le = LabelEncoder()
print(f'field Kecepatan Angin SEBELUM dilakukan label encoder\n {df["Kecepatan Angin"]}')

print()
df["Kecepatan Angin"]=le.fit_transform(df["Kecepatan Angin"])
df["Suhu"]=le.fit_transform(df["Suhu"])
df["Jenis Cuaca"]=le.fit_transform(df["Jenis Cuaca"])
print(f'field Kecepatan Angin SETELAH dilakukan label encoder\n {df["Kecepatan Angin"]}')
print()
print(f'SEMUA field SETELAH dilakukan label encoder\n {df}')

# X kapital bukan class label (bukan Jenis Cuaca)
X = df.iloc[:,0:2].values
Y = df.iloc[:,2:3].values
print('\n',X)
print('\n',Y)

X_train, X_test, y_train, y_test=train_test_split(X,df['Jenis Cuaca'],test_size=0.2,random_state=10)

klasifikasi=MultinomialNB().fit(X_train,y_train)
prediksi = klasifikasi.predict(X_test)


print('\n',f'Tingkat akurasi : ', accuracy_score(y_test,prediksi))
print()

print(classification_report(y_test,prediksi,zero_division=0))
print()
# rendah0, sedang1, tinggi2
# dingin0, normal1, panas2
# cerah0, hujan1, mendung2
# tinggi panas? 2,2

cuaca=[[2, 2]]
prediksi=klasifikasi.predict(cuaca)
prediksi_proba=klasifikasi.predict_proba(cuaca)
print(f'Hasil prediksi proba cuaca: ',prediksi_proba)
print()

for cari in prediksi:
    if cari==2:
        print('Hasil prediksi cuaca = MENDUNG')
    elif cari==1:
        print('Hasil prediksi cuaca = HUJAN')
    else:
        print('Hasil prediksi cuaca = CERAH')

print()
print(f'Hasil prediksi cuaca: ',prediksi)
print()