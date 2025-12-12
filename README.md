# Prediksi Hasil Panen Berbasis Fitur Agroklimat Menggunakan XGBoost

## 📌 Gambaran Proyek

Proyek ini bertujuan untuk memprediksi hasil panen dalam ton/hektar berdasarkan faktor agroklimat (suhu, curah hujan, cuaca) dan manajemen lahan (jenis tanah, penggunaan pupuk). Proyek ini dikembangkan sebagai Tugas Besar mata kuliah Machine Learning.

**Metode Utama:**

- **Algoritma:** XGBoost Regressor (dan Decision Tree sebagai baseline).
- **Explainability:** SHAP (SHapley Additive exPlanations).
- **Deployment:** Streamlit Web App.

## 📂 Struktur Direktori

- `data/`: Menyimpan dataset agrikultur (800 sampel).
- `notebooks/`: Jupyter Notebook untuk eksperimen EDA, Preprocessing, dan Modeling.
- `src/`: Source code aplikasi Streamlit.
- `models/`: File model yang telah dilatih (.json/.pkl).

## 🚀 Cara Menjalankan (Installation)

1.  **Clone repositori ini:**

    ```bash
    git clone [https://github.com/username-anda/nama-repo.git](https://github.com/username-anda/nama-repo.git)
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Jalankan Aplikasi Streamlit (Nanti di Minggu 4):**
    ```bash
    streamlit run src/app.py
    ```

## 📊 Hasil Analisis

(Bagian ini akan diupdate setelah Minggu 4, berisi screenshot grafik SHAP dan metrik evaluasi MAE/RMSE)
