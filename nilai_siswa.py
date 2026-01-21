nama = input("Masukkan Nama Siswa: ")
nilai = int(input("Masukkan Nilai Siswa: "))
kelas = input("Masukkan Kelas Siswa: ")

siswa = [
    {"nama":nama,"nilai":nilai,"kelas":kelas},
]

def cek_lulus(nilai):
    if nilai >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"
    
def rata_rata(nilai_list):
    return sum(nilai_list) / len(nilai_list)

print("Siswa yang lulus: ")
for data in siswa:
    if cek_lulus(data["nilai"]) == "Lulus":
        print(data["nama"], data["nilai"])

kelas_dict = {}

for data in siswa:
    kelas = data["kelas"]
    if kelas not in kelas_dict:
        kelas_dict[kelas] = []
        kelas_dict[kelas].append(data["nilai"])

for kelas, nilai_list in kelas_dict.items():
    print(f"Rata-rata kelas{kelas}:", rata_rata(nilai_list))
