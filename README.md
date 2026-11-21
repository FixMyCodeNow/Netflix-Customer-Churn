# Netflix Customer Churn Analysis

Analisis perilaku pelanggan Netflix untuk memahami faktor yang berkaitan dengan churn, membandingkan model klasifikasi, melakukan segmentasi pelanggan dengan clustering, dan menyajikan ringkasan interaktif melalui dashboard Streamlit.

## Isi Proyek

- `Netflix_Customer_Churn.ipynb` - eksplorasi data, analisis churn, klasifikasi, SHAP, dan segmentasi K-Means.
- `netflix_customer_churn.csv` - dataset mentah berisi 5.000 pelanggan.
- `data_bersih.csv` - dataset hasil pemrosesan, termasuk kelompok ketidakaktifan dan segmentasi pelanggan.
- `app.py` - dashboard Streamlit untuk memfilter tipe langganan dan melihat churn rate.
- `archive (7).zip` - arsip asli dataset mentah.

## Temuan Utama

Dataset tidak memiliki nilai kosong dan terdiri atas 5.000 pelanggan. Tingkat churn keseluruhan adalah **50,3%**.

| Tipe langganan | Rata-rata biaya bulanan | Tingkat churn | Jumlah pelanggan |
|---|---:|---:|---:|
| Basic | $8.99 | 61.83% | 1.661 |
| Standard | $13.99 | 45.44% | 1.646 |
| Premium | $17.99 | 43.71% | 1.693 |

Analisis kelompok ketidakaktifan menunjukkan korelasi yang kuat dengan churn: pelanggan yang tidak login selama 31-50 hari memiliki tingkat churn sekitar 72-78%.

### Perbandingan Model

Notebook membandingkan Logistic Regression dan XGBoost pada pembagian data 80% latih dan 20% uji.

| Model | ROC-AUC | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.966 | 0.875 | 0.905 | 0.890 |
| XGBoost | 1.000 | 0.996 | 0.988 | 0.992 |

SHAP digunakan pada model XGBoost untuk menilai kontribusi fitur terhadap prediksi churn.

### Segmentasi Pelanggan

K-Means membandingkan 2 sampai 6 cluster menggunakan `watch_hours`, `avg_watch_time_per_day`, `number_of_profiles`, dan `last_login_days`. Notebook memilih empat segmen berdasarkan analisis yang dilakukan.

| Segmen | Jam tontonan | Tontonan/hari | Hari sejak login | Rata-rata churn |
|---:|---:|---:|---:|---:|
| 0 | 8.17 | 0.53 | 27.37 | 61% |
| 1 | 7.54 | 0.35 | 33.75 | 57% |
| 2 | 23.88 | 9.36 | 1.92 | 0% |
| 3 | 35.09 | 1.44 | 33.40 | 3% |

## Instalasi

Syarat: Python 3.10 atau versi yang lebih baru.

```bash
git clone https://github.com/FixMyCodeNow/Netflix-Customer-Churn.git
cd Netflix-Customer-Churn

python -m venv .venv
source .venv/bin/activate
pip install pandas numpy matplotlib scikit-learn xgboost shap plotly streamlit jupyter
```

Untuk Windows, aktifkan environment virtual dengan:

```powershell
.venv\Scripts\activate
```

## Menjalankan Dashboard

Pastikan terminal berada pada direktori proyek, lalu jalankan:

```bash
streamlit run app.py
```

Dashboard menyediakan filter tipe langganan, kartu churn rate, jumlah pelanggan, dan grafik churn berdasarkan tipe langganan.

## Menjalankan Notebook

```bash
jupyter notebook Netflix_Customer_Churn.ipynb
```

Jalankan sel notebook secara berurutan agar variabel `df`, data latih/uji, model, dan hasil segmentasi tersedia saat bagian berikutnya dieksekusi.
