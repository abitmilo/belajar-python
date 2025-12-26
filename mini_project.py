#Buat function
def cek_nilai(nilai):
    if nilai >= 75 :
        return "Lulus"
    else:
        return "Tidak Lulus"

#Minta Jumlah Input Siswa
jumlah = int(input("Masukkan jumlah siswa: "))

#Loop input nilai siswa
nilai_siswa = []
for i in range(jumlah):
        nilai = int(input("masukkan nilai siswa: "))
        nilai_siswa.append(nilai)
        
#Loop + Function (output hasil)
for nilai in nilai_siswa:
    hasil = cek_nilai(nilai)
    print(nilai,"=>", hasil)