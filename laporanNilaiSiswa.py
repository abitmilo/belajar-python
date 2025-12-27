siswa = [
    {"nama" : "Andi", "nilai" : 80},
    {"nama" : "Budi", "nilai" : 60},
    {"nama" : "Cici", "nilai" : 90}
]

def cek_lulus(nilai):
    if nilai >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"

jumlah = int(input("masukkan jumlah siswa tambahan: "))
    

for i in range(jumlah):
    nama = input("Masukkan Nama Siswa: ")
    
    while True:
        nilai = int(input("Masukkan nilai(0 - 100): "))
        if 0 <= nilai <= 100 :
            break
        else: 
            print("Nilai Harus anatara 1 dan 100")
    
    siswa.append({
        "nama" : nama,
        "nilai" : nilai,
    })

print("Laporan Nilai Siswa")
for data in siswa :
    status = cek_lulus(data["nilai"])
    print(data["nama"], status)