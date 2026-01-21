import os

def cek_kelulusan(nilai):
    if nilai >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"
os.system("clear")
nama = input("Masukkan nama: ")
nilai = int(input("Masukkan nilai: "))

status = cek_kelulusan(nilai)

with open("siswa.txt", "a") as file:
    file.write(f"{nama},dengan nilai {nilai} dan status {status}\n")

print("Data berhasil disimpan")


with open("siswa.txt", 'r') as file:
    for baris in file:
        print(baris)