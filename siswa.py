siswa = []

def cek_kelulusan(nilai):
    if nilai >= 75:
        return 'Lulus'
    else:
        return 'Tidak Lulus'
    
def tambah_siswa():
    nama = input("Masukkan Nama: ")
    nilai = int(input("Masukkan nilai: "))
    siswa.append({
        'nama': nama,
        'nilai': nilai,
    })
    
tambah_siswa()
for s in siswa:
    status = cek_kelulusan(s['nilai'])
    print(s['nama'], '-', s['nilai'], '-', status)