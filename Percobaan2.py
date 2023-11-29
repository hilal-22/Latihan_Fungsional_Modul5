import matplotlib.pyplot as plt
import numpy as np

# Koordinat titik
xpoints = np.array([1, 8, 10])
ypoints = np.array([3, 10, 5])

# Ukuran grafik
plt.figure(figsize=(8, 6))

# Menambahkan garis plot dengan warna merah
plt.plot(xpoints, ypoints, color='red', marker='o', linestyle='-', linewidth=2, markersize=8, label='Garis Utama')

# Menambahkan titik-titik pada grafik untuk melengkapi
plt.scatter(xpoints, ypoints, color='blue', marker='s', s=50, label='Titik Data')

# Menambahkan label pada sumbu x dan y
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

# Menambahkan judul grafik
plt.title('Grafik dengan Variasi dan Informasi')

# Menambahkan grid
plt.grid(True, linestyle='--', alpha=0.7)

# Menambahkan legenda
plt.legend()

# Menetapkan batas sumbu x dan y
plt.xlim([0, 15])
plt.ylim([0, 15])

# Menampilkan grafik
plt.show()
