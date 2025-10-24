import pandas as pd
import matplotlib.pyplot as plt

# 🔹 1. Baca file CSV
df = pd.read_csv(
    r"C:\Users\k\Documents\Probstat\Jumlah Jemaah Haji yang Diberangkatkan ke Tanah Suci Mekah Menurut Kabupaten_Kota di Provinsi DKI Jakarta, 2024.csv"
)

# 🔹 2. Ambil kolom yang diperlukan
data = df[["Kabupaten/Kota", "Jemaah Haji"]].copy()

# 🔹 3. Bersihkan data
data["Jemaah Haji"] = pd.to_numeric(data["Jemaah Haji"], errors="coerce")
data = data.dropna(subset=["Jemaah Haji"])
data = data[~data["Kabupaten/Kota"].str.contains("DKI Jakarta", case=False, na=False)]

# 🔹 4. Hitung statistik deskriptif
mean_val = data["Jemaah Haji"].mean()
median_val = data["Jemaah Haji"].median()
mode_val = data["Jemaah Haji"].mode()[0]
variance_val = data["Jemaah Haji"].var()
std_val = data["Jemaah Haji"].std()

print("\n📊 Statistik Jemaah Haji DKI Jakarta (tanpa total):")
print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val}")
print(f"Mode: {mode_val}")
print(f"Variance: {variance_val:.2f}")
print(f"Standard Deviation: {std_val:.2f}")

# 🔹 5. Buat histogram dengan batang kurus dan warna biru langit
plt.figure(figsize=(9, 6))
n, bins, patches = plt.hist(
    data["Jemaah Haji"],
    bins=6,
    color="#5DADE2",          # 🌤️ biru langit lembut
    edgecolor="white",
    alpha=0.9,
    rwidth=0.4               # 🔸 batang lebih kurus
)

# 🔹 6. Tambahkan garis mean & median
plt.axvline(mean_val, color="#E74C3C", linestyle="--", linewidth=2, label=f"Mean = {mean_val:.0f}")
plt.axvline(median_val, color="#1F618D", linestyle=":", linewidth=2, label=f"Median = {median_val:.0f}")

# 🔹 7. Hias tampilan
plt.title("Distribusi Jumlah Jemaah Haji per Kabupaten/Kota\nProvinsi DKI Jakarta Tahun 2024",
          fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Jumlah Jemaah Haji", fontsize=12, labelpad=10)
plt.ylabel("Frekuensi (Jumlah Kabupaten/Kota)", fontsize=12, labelpad=10)
plt.legend(frameon=False, fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.4)

# 🔹 8. Tambahkan teks penanda
plt.text(mean_val + 50, plt.ylim()[1]*0.85, "← Mean", color="#E74C3C", fontsize=10)
plt.text(median_val - 100, plt.ylim()[1]*0.65, "Median →", color="#1F618D", fontsize=10, ha="right")

# 🔹 9. Latar belakang lembut
plt.gca().set_facecolor("#F8FBFF")
plt.tight_layout()
plt.show()
