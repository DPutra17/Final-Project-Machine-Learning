# Struktur MVC - Crop Yield Prediction System

## 🎯 Sudah Berhasil Diimplementasikan!

Aplikasi sekarang menggunakan **arsitektur MVC (Model-View-Controller)** yang lebih terstruktur dan modular.

### 📂 Struktur Folder Baru:

```
src/
├── app.py                          ← Aplikasi lama (legacy)
├── app_mvc.py                      ← Aplikasi baru dengan MVC ✨
│
├── config/                         ← Konfigurasi
│   └── settings.py                 • Paths, colors, constants
│
├── models/                         ← Layer Model (Data & Logic)
│   ├── model_loader.py             • Load ML models
│   └── data_loader.py              • Load datasets & metrics
│
├── views/                          ← Layer View (Halaman UI)
│   ├── __init__.py
│   ├── home.py                     ✅ Home page (sudah jadi)
│   ├── single_prediction.py        🚧 (belum)
│   ├── model_performance.py        🚧 (belum)
│   ├── shap_analysis.py            🚧 (belum)
│   ├── data_visualization.py       🚧 (belum)
│   ├── batch_prediction.py         🚧 (belum)
│   └── model_comparison.py         🚧 (belum)
│
├── components/                     ← Komponen UI Reusable
│   ├── sidebar.py                  • Sidebar navigation
│   └── cards.py                    • Card components
│
└── utils/                          ← Helper Functions
    ├── styling.py                  • CSS styling
    └── helpers.py                  • Helper functions
```

## 🚀 Cara Menjalankan

### Aplikasi MVC (Baru):
```bash
streamlit run src/app_mvc.py
```

### Aplikasi Original (Lama):
```bash
streamlit run src/app.py
```

## ✨ Keuntungan Arsitektur MVC

### 1. **Separation of Concerns**
- **Model** → Menangani data dan business logic
- **View** → Menangani tampilan UI
- **Components** → Komponen yang bisa dipakai ulang

### 2. **Mudah Di-maintain**
```python
# SEBELUM (app.py - 1600+ baris)
# Semua kode tercampur dalam 1 file

# SETELAH (MVC)
views/home.py           # 150 baris
models/model_loader.py  # 50 baris
components/sidebar.py   # 80 baris
# ... lebih terstruktur!
```

### 3. **Reusability (Pakai Ulang)**
```python
# Komponen bisa dipakai di banyak halaman
from components.cards import gradient_card

gradient_card("Title", "Description", "🎯", ['#667eea', '#764ba2'])
```

### 4. **Mudah Ditambahkan Fitur Baru**
```python
# 1. Buat file view baru
# views/new_page.py
def render():
    st.header("New Page")

# 2. Import di __init__.py
# 3. Tambahkan route di app_mvc.py
# Selesai!
```

## 📝 Contoh Penggunaan

### Model Layer:
```python
from models.model_loader import load_models, predict
from models.data_loader import load_dataset, load_metrics

# Load models
models = load_models()

# Load data
df = load_dataset()
metrics = load_metrics()

# Make prediction
prediction = predict(models['XGBoost'], 'XGBoost', features)
```

### View Layer:
```python
# views/my_page.py
import streamlit as st
from models.data_loader import load_dataset

def render():
    st.header("My Page")
    df = load_dataset()
    st.dataframe(df)
```

### Components:
```python
from components.cards import gradient_card, feature_card

# Gradient card
gradient_card("Accurate", "High precision", "🎯", ['#667eea', '#764ba2'])

# Feature card with button
if feature_card("🔮", "Prediction", "Make predictions", "Try Now", "btn_1"):
    st.success("Button clicked!")
```

## 🎨 Struktur File yang Sudah Jadi

| File | Status | Fungsi |
|------|--------|--------|
| `app_mvc.py` | ✅ | Entry point aplikasi |
| `config/settings.py` | ✅ | Konfigurasi & constants |
| `models/model_loader.py` | ✅ | Load ML models |
| `models/data_loader.py` | ✅ | Load datasets |
| `views/home.py` | ✅ | Home page view |
| `components/sidebar.py` | ✅ | Sidebar component |
| `components/cards.py` | ✅ | Card components |
| `utils/styling.py` | ✅ | CSS styling |
| `utils/helpers.py` | ✅ | Helper functions |

## 🚧 Yang Perlu Ditambahkan

Untuk menyelesaikan migrasi, perlu membuat view files untuk:

1. `views/single_prediction.py` - Form prediksi manual
2. `views/model_performance.py` - Analisis performa model
3. `views/shap_analysis.py` - SHAP explainability
4. `views/data_visualization.py` - Visualisasi data
5. `views/batch_prediction.py` - Batch prediction dari CSV
6. `views/model_comparison.py` - Perbandingan model

## 💡 Tips Development

### Menambahkan Halaman Baru:
1. Buat file di `views/` folder
2. Buat fungsi `render()`
3. Import di `views/__init__.py`
4. Tambahkan route di `app_mvc.py`
5. Tambahkan config di `settings.py`

### Membuat Component Baru:
1. Buat file di `components/` folder
2. Buat fungsi yang mengembalikan komponen
3. Import dan gunakan di view manapun

### Menambahkan Utility:
1. Buat fungsi di `utils/helpers.py`
2. Import di view yang membutuhkan

## 📊 Perbandingan Kode

### SEBELUM (Monolithic):
```python
# app.py - 1600+ baris
import streamlit as st
# ... semua imports

def main():
    # ... navigation
    if menu == "Home":
        # 150 baris kode home
    elif menu == "Prediction":
        # 200 baris kode prediction
    # ... dst
```

### SETELAH (MVC):
```python
# app_mvc.py - 70 baris
from views import home, prediction

def main():
    page = render_sidebar()
    if page == "Home":
        home.render()  # Clean!
    elif page == "Prediction":
        prediction.render()  # Clean!
```

## 🎉 Kesimpulan

Aplikasi sekarang lebih:
- ✅ **Terstruktur** - Kode terorganisir dengan baik
- ✅ **Maintainable** - Mudah dipelihara dan di-debug
- ✅ **Scalable** - Mudah ditambahkan fitur baru
- ✅ **Reusable** - Komponen bisa dipakai ulang
- ✅ **Testable** - Lebih mudah untuk testing
- ✅ **Collaborative** - Banyak developer bisa bekerja parallel

Selamat! Anda sekarang memiliki aplikasi dengan arsitektur yang professional! 🚀
