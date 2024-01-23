import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

def k_nn_prediction(X_train, y_train, X_test, y_test, n_neighbors):
    # print('-------' * 9)
    print('\nK = ', n_neighbors)
    
    knn_classifier = KNeighborsClassifier(n_neighbors)
    knn_classifier.fit(X_train, y_train)

    # Melakukan prediksi pada data uji
    predictions = knn_classifier.predict(X_test)

    # Evaluasi model
    accuracy = accuracy_score(y_test, predictions)
    classification_rep = classification_report(y_test, predictions, zero_division=0)

    print(f'Tingkat akurasi : {accuracy}')
    print('\n', classification_rep)

    # Contoh prediksi untuk data baru
    new_data = [[5, 7]]
    prediction = knn_classifier.predict(new_data)

    # Mapping kelas hasil prediksi ke kategori aslinya
    result_mapping = {2: 'TAMAN', 1: 'PANTAI', 0: 'GUNUNG'}
    result_category = result_mapping.get(prediction[0], 'Kategori tidak dikenal')
    print(f'Hasil prediksi wisata dengan K={n_neighbors}: {result_category}')
    print('-------' * 9)

# Contoh penggunaan fungsi
df = pd.read_excel('respon.xlsx', 'knn')
print(df)
print('-------' * 9)

le = LabelEncoder()

# Menggunakan LabelEncoder untuk mengubah data kategorikal menjadi numerik
df["Jarak_dari_Pusat_Kota"] = le.fit_transform(df["Jarak_dari_Pusat_Kota"])
df["Tingkat_Kepopuleran"] = le.fit_transform(df["Tingkat_Kepopuleran"])
df["Jenis_Tempat_Wisata"] = le.fit_transform(df["Jenis_Tempat_Wisata"])

X = df.iloc[:, 0:2].values
y = df["Jenis_Tempat_Wisata"].values

# Membagi dataset menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

n_neighbors1 = 3
n_neighbors2 = 5

k_nn_prediction(X_train, y_train, X_test, y_test, n_neighbors1)
k_nn_prediction(X_train, y_train, X_test, y_test, n_neighbors2)
