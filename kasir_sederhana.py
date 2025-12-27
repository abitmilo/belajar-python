# --- TUGAS HARI 1: KALKULATOR TOKO ---

print("=== KASIR SEDERHANA ===")

# 1. INPUT
# Minta user memasukkan nama barang (String)
nama_barang = input("Masukkan nama barang: ")

# Minta user memasukkan harga (Ingat! input() menghasilkan string, jadi harus di-casting ke int)
harga_barang = int(input("Masukkan harga barang (Rp): "))

# Minta user memasukkan jumlah barang (Ini juga harus angka)
jumlah_barang = int(input("Masukkan jumlah beli: "))

# 2. PROSES (LOGIKA)
# Hitung total harga (Harga dikali Jumlah)
# Ganti tanda tanya (?) dengan rumus matematika yang benar
total_bayar = harga_barang * jumlah_barang

# 3. OUTPUT
# Tampilkan hasil akhir menggunakan f-string
# Contoh format: Struk belanja: Kopi, Total: Rp 30000
print(f"Struk belanja: {nama_barang}, Total yang harus dibayar: Rp {total_bayar}")