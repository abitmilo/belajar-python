def cek_kelulusan(nilai):
    if nilai >= 90:
        return "Sangat Baik"
    elif nilai >= 75 <= 89:
        return "Lulus"
    else:
        return "Tidak Lulus"
value = int(input("masukkan Nilai anda"))
   
hasil = cek_kelulusan(value)
print(f'nilai anda adalah {value}. maka anda {hasil}')
