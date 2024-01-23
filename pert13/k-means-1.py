import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score
import matplotlib.pyplot as plt

data = pd.read_excel('data-tiga.xlsx')
print('\n',data,'\n')

# menerapkan algoritma K-Means, dengan 3 kelompok
km= KMeans(n_clusters=3, n_init=10,max_iter=100)
klaster = km.fit_predict(data[['X','Y']])
centroids= km.cluster_centers_
label = km.labels_

# centroid pada iterasi akhir
print(f'Labels : \n, {label}, \n')
print(f'Centroids : \n, {centroids}, \n')

# menghitung Davis-bouldin-index
ukur=davies_bouldin_score(data[['X','Y']],label)
print(f'nilai DBI : , {ukur}','\n')

# hasil cluster
data['Cluster']=klaster
print(f'Hasil Cluster :\n',data,'\n')

data1=data[data.Cluster==0]
print(f'data untuk cluster 0 : \n',data1,'\n')
data2=data[data.Cluster==1]
print(f'data untuk cluster 1 : \n',data2,'\n')
data3=data[data.Cluster==2]
print(f'data untuk cluster 2 : \n',data3,'\n')

# menampilkan data dalam sebaran grafik
plt.scatter(data1.X, data1['Y'],color='green')
plt.scatter(data2.X, data2['Y'],color='red')
plt.scatter(data3.X, data3['Y'],color='blue')
plt.scatter(centroids[:,0],centroids[:,1],marker='x',color='black')

plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# enter
print()