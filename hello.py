siswa_list = []

def cek_kelulusan(nilai):
    if nilai >= 90 or nilai <= 100:
        return "Sangat Baik"
    elif nilai >= 75:
        return "Baik"
    else:
        return "Tidak Lulus"
    
while True:
    print("Input Data Siswa")
    nama = input("Masukkan nama siswa : ")
    
    try:
        nilai = int(input("Masukkan Nilai : "))
    except ValueError:
        print("❌ Nilai Harus Angka!!!")
        continue
    status = cek_kelulusan(nilai)
    
    siswa = {
        "nama" : nama,
        "nilai" : nilai,
        "status" : status
    }
    
    siswa_list.append(siswa)
    
    lanjut = input("Tambah siswa lagi? (y/n): ")
    if lanjut.lower() != "y":
        break
    
print("---Data Siswa---") 
for data in siswa_list:
    print(
        "Nama", data["nama"],
        "Nilai", data["nilai"],
        "Status", data["status"]
        )