import pandas as pd
from sklearn.model_selection import train_test_split
import os

# ==========================================
# 1. LOAD DATA
# ==========================================
print("Loading data...")
# Load CSV dengan separator ';' dan decimal ','
df = pd.read_csv('data/dataset_800.csv', sep=';', decimal=',')
print(f"✅ Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print("-" * 30)

# ==========================================
# 2. PREVIEW DATA
# ==========================================
print("Dataset Preview:")
print(df.head())
print("\nData Info:")
print(df.info())
print("-" * 30)

# ==========================================
# 5. PREPROCESSING (DATA PREPARATION)
# ==========================================

# A. Pisahkan Fitur (X) dan Target (y)
# X adalah semua kolom KECUALI target
X = df.drop(columns=['Yield_tons_per_hectare'])
# y adalah target yang ingin diprediksi
y = df['Yield_tons_per_hectare']

# B. Ubah Boolean menjadi Angka (0 dan 1)
# Komputer lebih suka angka 1/0 daripada True/False
bool_cols = ['Fertilizer_Used', 'Irrigation_Used']
X[bool_cols] = X[bool_cols].astype(int)

# C. One-Hot Encoding untuk Kolom Kategori
# Mengubah teks (Crop, Soil, Weather) menjadi angka biner
# drop_first=True menghapus 1 kolom dummy untuk mencegah redundansi (praktik terbaik regresi)
X = pd.get_dummies(X, columns=['Crop', 'Soil_Type', 'Weather_Condition'], drop_first=True)

# Cek hasil perubahan
print("✅ Preprocessing Selesai!")
print(f"Jumlah Kolom Awal: 9")
print(f"Jumlah Kolom Setelah Encoding: {X.shape[1]}")
print("-" * 30)

# ==========================================
# 6. SPLIT DATA (Latih vs Uji)
# ==========================================
# Membagi data: 80% untuk Latihan (Train), 20% untuk Ujian (Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Statistik Pembagian Data:")
print(f"Data Latih (Train): {X_train.shape[0]} baris")
print(f"Data Uji (Test)   : {X_test.shape[0]} baris")
print("-" * 30)

# ==========================================
# 7. SIMPAN DATA (SAVE PROCESSED DATA)
# ==========================================
# Menyimpan data yang sudah bersih agar Minggu depan tinggal Load (tidak perlu cleaning lagi)

# Tentukan lokasi folder penyimpanan (sesuaikan dengan struktur folder Anda)
output_dir = 'data'

# Pastikan foldernya ada, kalau belum ada dibuatkan
os.makedirs(output_dir, exist_ok=True)

print(f"Menyimpan file ke folder '{output_dir}'...")

# Simpan ke 4 file CSV terpisah
X_train.to_csv(f'{output_dir}/X_train.csv', index=False)
X_test.to_csv(f'{output_dir}/X_test.csv', index=False)
y_train.to_csv(f'{output_dir}/y_train.csv', index=False)
y_test.to_csv(f'{output_dir}/y_test.csv', index=False)

print("✅ SUKSES! 4 File berikut telah tersimpan:")
print("   1. X_train.csv (Fitur Latih)")
print("   2. y_train.csv (Target Latih)")
print("   3. X_test.csv  (Fitur Uji)")
print("   4. y_test.csv  (Target Uji)")
print("\nSiap lanjut ke Minggu 3 (Modeling)!")
