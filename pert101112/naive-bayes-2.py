import streamlit as st
import os
from PIL import Image
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,precision_score,recall_score, f1_score, classification_report


img=Image.open('halaman.jpg')
st.image(img,width=700)

# Membuat header web
st.write('''
         # APLIKASI KELULUSAN MAHASISWA
         ## Berbasis Web Menggunakan Streamlit
''')

# streamlit run naive-bayes-2.py
# os.system('streamlit run naive-bayes-2.py')

# side bar
img2=Image.open('header.png')
st.sidebar.image(img2)
st.sidebar.header('Inputan atribut :')

# inputan
nama=st.sidebar.text_input('Masukan Nama : ',placeholder='Ketikan Nama dengan benar')
jurusan=st.sidebar.selectbox('Pilih Jurusan',('0-Bahasa','1-IPA','2-IPA'),placeholder='pilih Jurusan',index=None)
gender=st.sidebar.selectbox('Pilih Gender',('0-Pria','1-Wanita'),placeholder='pilih Gender',index=None)
sekolah=st.sidebar.selectbox('Pilih sekolah',('0-Luar','1-Pekalongan'),placeholder='pilih sekolah',index=None)
sks=st.sidebar.selectbox('Pilih jumlah sks',('0-kurang18','1-lebih18'),placeholder='pilih sks',index=None)
asisten=st.sidebar.selectbox('Pilih asisten',('0-tidak','1-ya'),placeholder='Pernah jadi asisten ?',index=None)


# Membuat tombol
tombol ='t'
if 'clicked' not in st.session_state:
    st.session_state.clicked=False

def click_button():
    st.session_state.clicked=True

st.sidebar.button('PREDIKSI',type='secondary',on_click=click_button)
# st.sidebar.button("Prediksi",type="primary", on_click=click_button)

if st.session_state.clicked:
    tombol='y'

# algoritma naive bayes
def hitung_naivebayes(atribut):
    nama_file='dataset_template_tugas.xlsx'
    sheet_names='dataset'
    daftar_sheet=pd.ExcelFile(nama_file).sheet_names
    df = pd.read_excel(nama_file, sheet_name= sheet_names)
    le = LabelEncoder()
    df["JURUSAN"]=le.fit_transform(df["JURUSAN"])
    df["GENDER"]=le.fit_transform(df["GENDER"])
    df["ASAL_SEKOLAH"]=le.fit_transform(df["ASAL_SEKOLAH"])
    df["RERATA_SKS"]=le.fit_transform(df["RERATA_SKS"])
    df["ASISTEN"]=le.fit_transform(df["ASISTEN"])
    df["STUDY"]=le.fit_transform(df["STUDY"])

    X = df.iloc[:,0:5].values
    Y = df.iloc[:,5:6].values
    X_train, X_test, y_train, y_test=train_test_split(X,df['STUDY'],test_size=0.2,random_state=10)

    klasifikasi=MultinomialNB().fit(X_train,y_train)
    # prediksi = klasifikasi.predict(X_test)
    prediksi = klasifikasi.predict(atribut)
    st.write('nilai prediksi ',prediksi)
    if prediksi == 1:
        st.write("hasil prediksi terlambat")
    else :
        st.write("hasil prediksi tepat")

    # for cari in prediksi:
    #     if cari =='1':
    #         st.write("hasil prediksi terlambat")
    #     else:
    #         st.write("hasil prediksi tepat")

    nilai_prob=klasifikasi.predict_proba(atribut)
    st.write("#### Nilai probabilitas kelas 0-tepat, 1-terlambat: ",nilai_prob)

if tombol =='y':
    # cek tombol
    # st.write("Tombol diklik")
    # membuat data inputan dari user
    data_input={
        'jurusan': jurusan,
        'gender': gender,
        'sekolah': sekolah,
        'sks': sks,
        'asisten': asisten,
        }
    st.write("Nama mahasiswa: ",nama)
    st.write(data_input)
    inputan=pd.DataFrame(data_input, index=[0])
    st.write(inputan)

    data_input_konversi={
        'jurusan': int(jurusan[0:1]),
        'gender': int(gender[0:1]),
        'sekolah': int(sekolah[0:1]),
        'sks': int(sks[0:1]),
        'asisten': int(asisten[0:1]),
        }
    st.write(data_input_konversi)

    atribut=pd.DataFrame(data_input_konversi, index=[0])
    hitung_naivebayes(atribut)