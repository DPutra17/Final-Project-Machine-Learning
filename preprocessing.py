import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import os

# ==========================================
# 1. LOAD DATASET (Format Indonesia)
# ==========================================
# PENTING: Kita tambah parameter sep=';' dan decimal=',' 
# agar Python tidak bingung membaca file Anda.
print("Loading data...")
df = pd.read_csv('data/dataset_800.csv', sep=';', decimal=',')
print(f"✅ Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print("-" * 30)

# Cek apakah data sudah terbaca dengan benar (Harusnya tipe float64)
print("\nInfo Data:")
print(df.info())

print("\nCuplikan Data (Cek Angka Desimal):")
print(df.head())
print("-" * 30)

# ==========================================
# 2. EDA: ANALISIS TARGET (YIELD)
# ==========================================
plt.figure(figsize=(8, 5))
sns.histplot(df['Yield_tons_per_hectare'], kde=True, color='forestgreen')
plt.title('Distribusi Hasil Panen (Yield)')
plt.xlabel('Yield (Ton/Hektar)')
plt.ylabel('Frequency')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print("\n💡 Temuan Menarik:")
print("   Data terdistribusi normal dengan sedikit variasi")
print(f"   Range: {df['Yield_tons_per_hectare'].min():.2f} - {df['Yield_tons_per_hectare'].max():.2f} ton/ha")
print("-" * 30)

# ==========================================
# 3. EDA: KORELASI FITUR (HEATMAP)
# ==========================================
plt.figure(figsize=(10, 8))
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matriks Korelasi Antar Fitur')
plt.tight_layout()
plt.show()

print("\n📊 Korelasi tertinggi dengan Yield:")
yield_corr = correlation['Yield_tons_per_hectare'].sort_values(ascending=False)
for col, val in yield_corr.items():
    if col != 'Yield_tons_per_hectare':
        print(f"   {col:25s}: {val:+.3f}")
print("-" * 30)

# ==========================================
# 4. EDA: ANALISIS CUACA & TANAMAN
# ==========================================
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Grafik 1: Yield vs Tanaman
sns.barplot(x='Crop', y='Yield_tons_per_hectare', data=df, ax=axes[0], palette='viridis', errorbar=None)
axes[0].set_title('Rata-rata Yield per Tanaman')
axes[0].tick_params(axis='x', rotation=45)
axes[0].set_ylabel('Yield (ton/ha)')
axes[0].grid(axis='y', alpha=0.3)

# Grafik 2: Yield vs Cuaca
sns.boxplot(x='Weather_Condition', y='Yield_tons_per_hectare', data=df, ax=axes[1], palette='Set2')
axes[1].set_title('Sebaran Yield berdasarkan Cuaca')
axes[1].set_ylabel('Yield (ton/ha)')
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

print("\n🌾 Rata-rata Yield per Tanaman:")
print(df.groupby('Crop')['Yield_tons_per_hectare'].mean().sort_values(ascending=False))

print("\n🌦️ Rata-rata Yield per Kondisi Cuaca:")
print(df.groupby('Weather_Condition')['Yield_tons_per_hectare'].mean().sort_values(ascending=False))
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
