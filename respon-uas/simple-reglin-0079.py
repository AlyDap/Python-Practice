import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import math

data=pd.read_excel('respon.xlsx','simple-reglin')
print(data,'\n')

# ambil variabel x dan y pada data
X_train=data.iloc[:,:1].values
print(f'variabel X : \n {X_train}','\n')
y_train=data.iloc[:,1].values
print(f'variabel Y : \n {y_train}','\n')

# terapkan Linier regresi
reg=LinearRegression()
reg.fit(X_train,y_train)

# mencari variabel 'coefficient' $ 'Intercept'
print(f'Coefficient : {str(reg.coef_)}','\n')
print(f'Intercept : {str(reg.intercept_)}','\n')

pred=reg.predict(X_train)
print(f'Hasil prediksi : \n {pred}','\n')

print('Coefficient of Determination : %.2f' % r2_score(y_train,pred),'\n')
print('Mean Square Error : %.2f' % mean_squared_error(y_train,pred),'\n')
print('Root Mean Square Error : %.2f' % math.sqrt(mean_squared_error(y_train,pred)),'\n')

# harga tiket = X = variabel memengaruhi
# jumlah penontoh = Y = variabel dipengaruhi

# Mencari nilai Y berdasarkan nilai X
cek =[[30]]
pred=reg.predict(cek)
print(f'Hasil Prediksi X{cek} = Y{pred}','\n')

# Mencari nilai X berdasarkan nilai Y
cek_y = [750]
pred_x = (cek_y - reg.intercept_) / reg.coef_
print(f'Hasil prediksi Y{cek_y} = X{pred_x}', '\n')