import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([5, 9, 4, 8])

# Plot garis dengan warna yang berbeda
plt.plot(y1, label='Garis 1', color='red')
plt.plot(y2, label='Garis 2', color='blue')
plt.plot(y3, label='Garis 3', color='green')

# Menambahkan judul dan label pada sumbu x dan y
plt.title('Plot Tiga Garis dengan Warna Berbeda')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

# Menampilkan legenda
plt.legend()

# Menampilkan plot
plt.show()
