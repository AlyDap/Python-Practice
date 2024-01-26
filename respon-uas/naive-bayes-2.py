import streamlit as st
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
# side bar
img2=Image.open('header.png')
st.sidebar.image(img2)
st.sidebar.header('Inputan atribut :')

# inputan
# nama=st.sidebar.text_input('Masukan Nama : ',placeholder='Ketikan Nama dengan benar')
kecepatan_angin=st.sidebar.selectbox('Pilih Kecepatan Angin',('0-Rendah','1-Sedang','2-Tinggi'),placeholder='pilih Kecepatan Angin',index=None)
suhu=st.sidebar.selectbox('Pilih Suhu',('0-Dingin','1-normal','2-Panas'),placeholder='pilih Suhu',index=None)

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
    df=pd.read_excel('respon.xlsx','nb')
    le = LabelEncoder()
    df["Kecepatan Angin"]=le.fit_transform(df["Kecepatan Angin"])
    df["Suhu"]=le.fit_transform(df["Suhu"])

    X = df.iloc[:,0:2].values
    Y = df.iloc[:,2:3].values
    X_train, X_test, y_train, y_test=train_test_split(X,df['Jenis Cuaca'],test_size=0.2,random_state=10)

    klasifikasi=MultinomialNB().fit(X_train,y_train)
    # prediksi = klasifikasi.predict(X_test)
    prediksi = klasifikasi.predict(atribut)
    st.write('nilai prediksi ',prediksi)
    if prediksi == 0:
        st.write("hasil prediksi Cuaca Cerah")
    elif prediksi == 1:
        st.write("hasil prediksi Cuaca Hujan")
    elif prediksi == 2:
        st.write("hasil prediksi Cuaca Mendung")

    nilai_prob=klasifikasi.predict_proba(atribut)
    st.write("#### Nilai probabilitas cuaca 0-cerah, 1-hujan, 2-mendung: ",nilai_prob)

if tombol =='y':
    # cek tombol
    # st.write("Tombol diklik")
    # membuat data inputan dari user
    data_input={
        'kecepatan_angin': kecepatan_angin,
        'suhu': suhu,
        }
    # st.write("Nama mahasiswa: ",nama)
    st.write(data_input)
    inputan=pd.DataFrame(data_input, index=[0])
    st.write(inputan)

    data_input_konversi={
        'kecepatan_angin': int(kecepatan_angin[0:1]),
        'suhu': int(suhu[0:1]),
        }
    st.write(data_input_konversi)

    atribut=pd.DataFrame(data_input_konversi, index=[0])
    hitung_naivebayes(atribut)