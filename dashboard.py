import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu

@st.cache_data
#Load Data CSV
def load_data(url) :
    df = pd.read_csv(url)
    return df

def Analisis_data(df_data) :
    #Mengabil data order dengan status 'delivered'
    df_yeardate = df_data

    #Menghapus nilai null pada atribut 'order_delivered_customer_date' pada dataframe
   

    #Perhitungan value_count() untuk status 'processing','shipped','delivered'
    count_2013 = df_yeardate['year'].value_counts()[2013]
    count_2014 = df_yeardate['year'].value_counts()[2014]
    count_2015 = df_yeardate['year'].value_counts()[2015]
    count_2016 = df_yeardate['year'].value_counts()[2016]
    count_2017 = df_yeardate['year'].value_counts()[2017]


#Grafik Status Pengiriman
    data_tahun = pd.DataFrame({
        'Tahun': ['2013', '2014', '2015', '2016', '2017'],
        'Jumlah': [count_2013, count_2014, count_2015,count_2016,count_2017]
    })

    st.header("Grafik Data Tahunan Tiantian")
    st.dataframe(data_tahun)

 # Membuat pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(
        data_tahun['Jumlah'], 
        labels=data_tahun['Tahun'], 
        autopct='%1.1f%%', explode=[0.1, 0, 0, 0, 0], )
    plt.title('Data Tahun Tiantian')
    st.pyplot(plt)

    with st.expander("Penjelasan Data Tahun Tiantian") :
        st.write('Berdasarkan analisis pada data quality air tiantian terdapat beberapa data dari tahun 2013 sampai tahun 2017.data tahun 2013 terhitung ada 7340 dengan persentase 20.3%,data tahun 2014 terhitung ada 8760 dengan persentase 25.0%,data tahun 2015 terhitung ada 8760 dengan persentase 25.0%,data tahun 2016 terhitung ada 8784 dengan persentase 25.1%,dan data tahun 2017 terhitung ada 1416 dengan persentase 4.0%')
    
    df_temp = df_data

    count_temp = df_temp.nsmallest(4, 'TEMP')

    data_temp = pd.DataFrame({
        'Temp': ['TEMP'],
        'Jumlah': [count_temp['TEMP']]
    })

    st.header("Grafik Data TEMP Terendah")
    st.dataframe(data_temp.head())

    lowest_temps = df_temp.nsmallest(4, 'TEMP')

        # Plot menggunakan Matplotlib
    fig, ax = plt.subplots()
    ax.bar(lowest_temps['No'], lowest_temps['TEMP'], color='blue')
    ax.set_xlabel('Nomor Data')
    ax.set_ylabel('Suhu (°C)')
    ax.set_title('4 Nilai Terendah Suhu')
    ax.grid(True)
    st.pyplot(fig)

    with st.expander("Penjelasan Data TEM Terendah Tiantian") :
        st.write('Berdasarkan analisis pada data terkecil temperatur(TEMP) pada dataset quality air tiantian,terdapat 4 data terkecil dari keselurahan yaitu dengan temperatur (-16.2,-16.3,-16.8)')

    df_templargest = df_data

    count_templargest = df_templargest.nlargest(4, 'TEMP')

    data_temp = pd.DataFrame({
        'Temp': ['TEMP'],
        'Jumlah': [count_templargest['TEMP']]
    })

    st.header("Grafik Data TEMP Tertinggi")
    st.dataframe(data_temp.head())

    largest_temps = df_templargest.nlargest(4, 'TEMP')

        # Plot menggunakan Matplotlib
    fig, ax = plt.subplots()
    ax.bar(largest_temps['No'], largest_temps['TEMP'], color='green')
    ax.set_xlabel('Nomor Data')
    ax.set_ylabel('Suhu (°C)')
    ax.set_title('4 Nilai Tertinggi Suhu')
    ax.grid(True)
    st.pyplot(fig)

    with st.expander("Penjelasan Data TEMP Tertinggi Tiantian") :
        st.write('Berdasarkan analisis pada data terbesar temperatur(TEMP) pada dataset quality air tiantian,terdapat 4 data terbesar dari keselurahan yaitu dengan temperatur (41.1,40.4,40,39.6)')


def Analisis_Polusi(df_datatian):
    df_polusi = df_datatian
    
    rata_rata_polusi_per_bulan = df_polusi.groupby('month')['SO2'].mean()

    data_polusi = pd.DataFrame(
        {'Temp': ['SO2'],
        'Jumlah': [rata_rata_polusi_per_bulan]})

    st.header("Grafik Data SO2 Perbulan")
    st.dataframe(data_polusi.head())


    fig, ax = plt.subplots()
    ax.plot(rata_rata_polusi_per_bulan,marker='o', linestyle='-', color='green')
    ax.set_xlabel('')
    ax.set_ylabel('SO2')
    ax.set_title('SO2 Perbulan')
    ax.grid(True)
    st.pyplot(fig)

    with st.expander("Penjelasan Data SO2 Perbulan Tiantian") :
        st.write(':Berdasarkan analisis pada data peningkatan polusi perbulan(SO2) pada dataset quality air tiantian,peningkatanya dari bulan ke 1 sampai ke bulan 12 yaitu dari 27.4 sampai 18.5')


    rata_rata_polusi_per_tahun = df_polusi.groupby('year')['CO'].mean()

    data_polusi = pd.DataFrame(
        {'Temp': ['CO'],
        'Jumlah': [rata_rata_polusi_per_tahun]})

    st.header("Grafik Data CO Pertahun")
    st.dataframe(data_polusi.head())


    fig, ax = plt.subplots()
    ax.plot(rata_rata_polusi_per_tahun,marker='o', linestyle='-', color='green')
    ax.set_xlabel('')
    ax.set_ylabel('CO')
    ax.set_title('CO Pertahun')
    ax.grid(True)
    st.pyplot(fig)

    with st.expander("Penjelasan Data CO Pertahun Tiantian") :
        st.write('Berdasarkan analisis pada data perubahan karbon dioksida (CO) pada dataset quality air tiantian,peningkatanya dari tahun 2013 sampai ke tahun 2017 yaitu dari 1316.41 sampai 1724.27')

df_data = load_data("https://raw.githubusercontent.com/FarkhanEka/Tugas_Streamlit/main/PRSA_Data_Tiantan_20130301-20170228.csv")
df_datatian = load_data("https://raw.githubusercontent.com/FarkhanEka/Tugas_Streamlit/main/PRSA_Data_Tiantan_20130301-20170228.csv")
    




with st.sidebar :
    selected = option_menu('Menu',['Dashboard'],
    icons =["easel2", "graph-up"],
    menu_icon="cast",
    default_index=0)
    
if (selected == 'Dashboard') :
    st.header(f"Dashboard Analisis E-Commerce")
    tab1,tab2 = st.tabs(["Analisis Data Tahunan & Temperatur", "Analisis Carbon Dioksida & Polusi"])

    with tab1 :
        Analisis_data(df_data)

    with tab2:
        Analisis_Polusi(df_data)
    


