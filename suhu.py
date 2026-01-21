def tambah_siswa():
    nama = input("Masukkan nama: ")
    nilai = int(input("Masukkan nilai: "))
    return nama, nilai

nama, nilai = tambah_siswa()

print(nama)
print(nilai)