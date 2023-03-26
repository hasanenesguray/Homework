import streamlit as st
import pandas as pd
import datetime


# Sayfa Ayarları
st.set_page_config(
    page_title="Sinemmetre",
    page_icon="WhatsApp.jpeg",
    menu_items={
        "Get help": "mailto:hasanenesguray@gmail.com",
        "About": "For More Information\n" + "https://github.com/hasanenesguray/IDSA-DSBootcamp"
    }
)

# Başlık Ekleme
st.title("Hasan Sinem'i ne kadar seviyor?")

st.image("/Users/hasanenesguray/Desktop/Mavi/IMG-20220707-WA0003.jpg")

# Sidebarda Markdown Oluşturma
st.sidebar.markdown("Hasan **Sinem'i** 100 üzerinden ne kadar seviyor?")

# Sidebarda Kullanıcıdan Girdileri Alma
sevgi = st.sidebar.slider("Sevgimetre", 0, 100, 1)



# Sonuç Ekranı
if st.sidebar.button("Submit"):
    
    if sevgi == 100:
        st.header("Bildiniz!")
        st.image("IMG-20220829-WA0005.jpg")
        st.image("IMG-20220726-WA0007.jpg")
        st.image("IMG-20220704-WA0010.jpg")
        st.image("IMG-20220704-WA0009.jpg")
        st.image("IMG-20220624-WA0006.jpg")
        st.image("IMG-20220624-WA0001.jpg")
        st.image("IMG-20220622-WA0013.jpg")
        st.image("IMG-20220610-WA0000.jpg")
        st.image("IMG_20220902_163044.jpg")
    else:
        st.header("Bilemediniz, lütfen tekrar deneyiniz!")

else:
    st.markdown("Please click the *Submit Button*!")
