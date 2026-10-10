import numpy as np
from scipy.optimize import linprog

# PARAMETER
produk     = ["Media Agar Cokelat", "Media Agar Hijau"]
keuntungan = [25000, 30000]          # Rp per liter
bahan      = ["Nutrisi organik", "Hormon pertumbuhan"]
kebutuhan  = [
    [2, 1],  # 2x + 1y <= 16
    [1, 3]   # 1x + 3y <= 18
]
stok       = [16, 18]                # gram bahan tersedia

# OPTIMASI
res = linprog([-k for k in keuntungan], A_ub=kebutuhan, b_ub=stok, bounds=(0, None), method="highs")

# OUTPUT
print("HASIL OPTIMASI:")
for p, val in zip(produk, res.x):
    print(f"  {p:<25}: {val:.2f} liter")
print(f"  Keuntungan Maksimum      : Rp {-res.fun:,.0f}\n")

# PEMERIKSAAN KETERSEDIAAN BAHAN
print("PEMERIKSAAN PENGGUNAAN BAHAN:")
for b, koef, s in zip(bahan, kebutuhan, stok):
    terpakai = sum(a * x for a, x in zip(koef, res.x))
    status = "Habis terpakai" if np.isclose(terpakai, s) else f"Sisa {s - terpakai:.2f} gram"
    print(f"  - {b:<20}: {terpakai:.2f} / {s} gram ({status})")