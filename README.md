[histogram_haji.py](https://github.com/user-attachments/files/23121326/histogram_haji.py)
import pandas as pd
import matplotlib.pyplot as plt

# 🔹 1. Baca file CSV (pastikan path-nya benar)
df = pd.read_csv(r"C:\Users\k\Documents\Probstat\Jumlah Jemaah Haji yang Diberangkatkan ke Tanah Suci Mekah Menurut Kabupaten_Kota di Provinsi DKI Jakarta, 2024.csv"
)

# 🔹 2. Lihat struktur data
print("Kolom yang tersedia:", df.columns.tolist())
print(df.head())

# 🔹 3. Ambil kolom yang diperlukan
data = df[["Kabupaten/Kota", "Jemaah Haji"]].copy()

# 🔹 4. Pastikan kolom angka bertipe numerik
data["Jemaah Haji"] = pd.to_numeric(data["Jemaah Haji"], errors="coerce")

# 🔹 5. Hitung statistik deskriptif
mean_val = data["Jemaah Haji"].mean()
median_val = data["Jemaah Haji"].median()
mode_val = data["Jemaah Haji"].mode()[0]
variance_val = data["Jemaah Haji"].var()
std_val = data["Jemaah Haji"].std()

print("\n📊 Statistik Jemaah Haji DKI Jakarta:")
print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val}")
print(f"Mode: {mode_val}")
print(f"Variance: {variance_val:.2f}")
print(f"Standard Deviation: {std_val:.2f}")

# 🔹 6. Buat diagram batang
plt.figure(figsize=(8, 5))
plt.bar(data["Kabupaten/Kota"], data["Jemaah Haji"], color="mediumseagreen")

plt.title("Jumlah Jemaah Haji Diberangkatkan ke Tanah Suci (Provinsi DKI Jakarta)")
plt.xlabel("Kabupaten/Kota")
plt.ylabel("Jumlah Jemaah Haji")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()
