nama = input("nama pelamar ")
umur = int(input("Umur pelamar "))
nilai = int(input("Nilai Tes (1-100) "))

if umur >= 20 :
    if nilai >= 70 :
        hasil = "Lulus"
    else:
        hasil = "Tidak Lulus"
else:
    hasil = "Gagal (Umur Belum Cukup)"
    
print(f"Hasil Seleksi {nama} : {hasil}")       
