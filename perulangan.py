def cek_kelulusan(nilai):
    if nilai >= 90:
        return "Sangat Baik"
    elif nilai >= 75:
        return "Lulus"
    elif nilai < 50:
        return "Remedial"
    else:
        return "Tidak Lulus"
    
siswa_nilai = cek_kelulusan(51)
print(siswa_nilai)