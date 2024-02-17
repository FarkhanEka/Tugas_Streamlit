import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu



def Analisis_Pengiriman(df_year) :
    #Mengabil data order dengan status 'delivered'
    df_yeardate = df_year[df_year['year']]

    #Menghapus nilai null pada atribut 'order_delivered_customer_date' pada dataframe
    df_yeardate = df_yeardate.dropna(subset=['PM2.5','PM10','SO2','NO2','CO','O3','TEMP','PRES','DEWP','RAIN','wd','WSPM','station'])

    #Perhitungan value_count() untuk status 'processing','shipped','delivered'
    count_2013 = df_year['year'].value_counts()['2013']
    count_2014 = df_year['year'].value_counts()['2014']
    count_2015 = df_year['year'].value_counts()['2015']
    count_2016 = df_year['year'].value_counts()['2016']
    count_2017 = df_year['year'].value_counts()['2017']


#Grafik Status Pengiriman
    data_tahun = pd.DataFrame({
        'Tahun': ['2013', '2014', '2015', '2016', '2017'],
        'Jumlah': [count_2013, count_2014, count_2015,count_2016,count_2017]
    })

 #Perkembangan Pengiriman
    st.header("Grafik Jumlah Data Tiantian")
    st.dataframe(data_tahun)

    # Buat bar chart
    label = data_tahun['Tahun']
    data = data_tahun['Jumlah']


    df_data = load_data("https://raw.githubusercontent.com/FarkhanEka/Tugas_Streamlit/PRSA_Data_Tiantan_20130301-20170228.csv")

 #Perkembangan Pengiriman
    st.header("Grafik Perkembangan Pengiriman")
    st.dataframe(data_tahun)

    # Buat bar chart
    label = data_tahun['Kategori']
    data = data_tahun['Jumlah']



with st.sidebar :
    selected = option_menu('Menu',['Dashboard'],
    icons =["easel2", "graph-up"],
    menu_icon="cast",
    default_index=0)
    
if (selected == 'Dashboard') :
    st.header(f"Dashboard Analisis E-Commerce")
    tab1,tab2 = st.tabs(["Analisis Pengiriman", "Analisis Review"])

    with tab1 :
        Analisis_Pengiriman(df_year)


