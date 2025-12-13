# Prediksi Hasil Panen Berbasis Fitur Agroklimat Menggunakan XGBoost

## 📌 Gambaran Proyek

Proyek ini bertujuan untuk memprediksi hasil panen dalam ton/hektar berdasarkan faktor agroklimat (suhu, curah hujan, cuaca) dan manajemen lahan (jenis tanah, penggunaan pupuk). Proyek ini dikembangkan sebagai Tugas Besar mata kuliah Machine Learning.

**Metode Utama:**

- **Algoritma:** XGBoost, LightGBM, Random Forest, dan Decision Tree
- **Explainability:** SHAP (SHapley Additive exPlanations)
- **Deployment:** Streamlit Web App

## 📂 Struktur Direktori

```
Final-Project-Machine-Learning/
├── data/
│   ├── dataset_800.csv         # Dataset asli (800 sampel)
│   ├── X_train.csv             # Data training features
│   ├── X_test.csv              # Data testing features
│   ├── y_train.csv             # Data training target
│   └── y_test.csv              # Data testing target
├── notebooks/
│   ├── EDA_Preprocessing.ipynb          # Exploratory Data Analysis
│   ├── Baseline_Model.ipynb             # Model Baseline (Decision Tree)
│   ├── Complete_ML_Pipeline.ipynb       # Pipeline Lengkap ML
│   └── Final_Model_XGBoost.ipynb        # Model Final XGBoost
├── models/
│   ├── decision_tree.pkl       # Model Decision Tree
│   ├── random_forest.pkl       # Model Random Forest
│   ├── xgboost_model.json      # Model XGBoost
│   ├── lightgbm_model.txt      # Model LightGBM
│   ├── model_comparison.csv    # Perbandingan Metrik Model
│   └── week_4_config.json      # Konfigurasi Model
├── src/
│   └── app.py                  # Aplikasi Streamlit
├── requirements.txt            # Dependencies Python
└── README.md                   # Dokumentasi Proyek
```

## 🚀 Cara Menjalankan

### Prerequisites
- Python 3.13 atau lebih tinggi
- pip (Python package manager)

### Installation

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/username-anda/Final-Project-Machine-Learning.git
   cd Final-Project-Machine-Learning
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Aplikasi Streamlit:**
   ```bash
   streamlit run src/app.py
   ```
   
   Atau jika menggunakan Python secara langsung:
   ```bash
   python -m streamlit run src/app.py
   ```

4. **Akses Aplikasi:**
   - Buka browser dan akses: `http://localhost:8501`
   - Atau gunakan Network URL untuk akses dari perangkat lain

## 📊 Fitur Aplikasi

### 1. 🏠 Home
- Informasi umum tentang proyek
- Deskripsi dataset dan fitur yang digunakan

### 2. 📈 Model Performance
- Perbandingan performa model (R², MAE, RMSE, MAPE)
- Visualisasi metrik evaluasi
- Grafik perbandingan antar model

### 3. 🔮 Prediction
- Form input untuk prediksi hasil panen
- Input fitur: Region, Soil Type, Crop Type, Rainfall, Temperature, Fertilizer, Irrigation, Weather Condition
- Hasil prediksi dari model terbaik (XGBoost/LightGBM)

### 4. 🔍 SHAP Analysis
- SHAP Summary Plot: Pengaruh global fitur terhadap prediksi
- SHAP Feature Importance: Ranking fitur berdasarkan dampak
- Interpretasi model secara visual

## 🛠️ Dependencies

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- lightgbm
- shap
- streamlit

## 📊 Hasil Analisis

### Model Performance
Aplikasi ini menyediakan perbandingan performa dari 4 model machine learning:
- Decision Tree (Baseline)
- Random Forest
- XGBoost
- LightGBM

### Metrik Evaluasi
- **R² (R-Squared):** Mengukur proporsi variansi yang dijelaskan oleh model
- **MAE (Mean Absolute Error):** Rata-rata error absolut
- **RMSE (Root Mean Squared Error):** Akar dari rata-rata kuadrat error
- **MAPE (Mean Absolute Percentage Error):** Persentase error rata-rata

### SHAP Analysis
SHAP digunakan untuk menjelaskan kontribusi setiap fitur terhadap prediksi model, memberikan transparansi dan interpretabilitas pada model machine learning.

## 👥 Tim Pengembang

Proyek ini dikembangkan sebagai Tugas Besar mata kuliah Machine Learning.

## 📝 Lisensi

Project ini dibuat untuk keperluan akademik.
