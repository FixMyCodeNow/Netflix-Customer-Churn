import streamlit as st                                # library untuk membuat web dashboard
import pandas as pd                                   # membaca dan mengolah data
import plotly.express as px                           # membuat grafik interaktif

df = pd.read_csv("data_bersih.csv")                   # baca data yang tadi disimpan
st.title("Netflix Customer Churn Dashboard")          # judul di bagian atas halaman

plan = st.multiselect(                                # filter pilihan ganda di halaman
    "Subscription type",                              # label filter
    df["subscription_type"].unique(),                 # pilihan: semua jenis plan yang ada
    default=list(df["subscription_type"].unique()),   # awalnya semua plan terpilih
)
d = df[df["subscription_type"].isin(plan)]            # saring data sesuai plan yang dipilih

c1, c2 = st.columns(2)                                # buat dua kolom berdampingan
c1.metric("Churn rate", f"{d['churned'].mean()*100:.1f}%")  # kartu angka: persentase churn
c2.metric("Jumlah pelanggan", len(d))                 # kartu angka: banyaknya pelanggan

churn_plan = (                                        # hitung churn rate per plan untuk grafik
    d.groupby("subscription_type")["churned"].mean().mul(100).reset_index()
)
st.plotly_chart(                                      # tampilkan grafik di dashboard
    px.bar(churn_plan, x="subscription_type", y="churned")  # grafik batang: churn rate tiap plan
)