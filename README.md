# Netflix Customer Churn Analysis

Analisis perilaku pelanggan Netflix untuk memahami faktor yang berkaitan dengan churn, membandingkan model klasifikasi, melakukan segmentasi pelanggan dengan clustering, dan menyajikan ringkasan interaktif melalui dashboard Streamlit.

**Aplikasi live:** [Buka Netflix Customer Churn Dashboard](https://fixmycodenow-netflix-customer-churn-app-qqekf7.streamlit.app/)

## Isi Proyek

- `Netflix_Customer_Churn.ipynb` - eksplorasi data, analisis churn, klasifikasi, SHAP, dan segmentasi K-Means.
- `netflix_customer_churn.csv` - dataset mentah berisi 5.000 pelanggan.
- `data_bersih.csv` - dataset hasil pemrosesan, termasuk kelompok ketidakaktifan dan segmentasi pelanggan.
- `app.py` - dashboard Streamlit untuk memfilter tipe langganan dan melihat churn rate.
- `requirements.txt` - dependensi Python untuk menjalankan dashboard dan deploy di Streamlit Community Cloud.


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

## Instalasi Lokal

Syarat: Python 3.10 atau versi yang lebih baru.

```bash
git clone https://github.com/FixMyCodeNow/Netflix-Customer-Churn.git
cd Netflix-Customer-Churn

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Untuk Windows, aktifkan environment virtual dengan:

```powershell
.venv\Scripts\activate
```

Kemudian jalankan dashboard:

```bash
streamlit run app.py
```

Dashboard menyediakan filter tipe langganan, kartu churn rate, jumlah pelanggan, dan grafik churn berdasarkan tipe langganan.

## Deploy ke Streamlit Community Cloud

1. Pastikan repository berisi `app.py`, `requirements.txt`, dan `data_bersih.csv` di branch yang akan dideploy.
2. Buka [Streamlit Community Cloud](https://share.streamlit.io/) dan hubungkan akun GitHub.
3. Pilih **Create app**, lalu pilih repository `FixMyCodeNow/Netflix-Customer-Churn`, branch `main`, dan file utama `app.py`.
4. Klik **Deploy**. Streamlit akan memasang dependensi dari `requirements.txt` dan menjalankan aplikasi.

Jika file utama atau branch berbeda, sesuaikan pilihannya sebelum deploy. `requirements.txt` harus berada di root repository agar terdeteksi otomatis.

## Menjalankan Notebook

```bash
jupyter notebook Netflix_Customer_Churn.ipynb
```

Notebook analisis menggunakan beberapa paket tambahan yang tidak diperlukan oleh dashboard. Jika ingin menjalankan seluruh notebook, pasang juga dependensi analisis seperti `numpy`, `matplotlib`, `scikit-learn`, `xgboost`, `shap`, dan `jupyter`.
