nama = input("Masukkan nama")
nilai = input("Masukkan Nilai")
Kelas = input("Masukkan Kelas")

siswa = [
    {"nama":"Andi","nilai":80,"kelas":"X"},
    {"nama":"Budi","nilai":60,"kelas":"X"},
    {"nama":"Cici","nilai":90,"kelas":"XI"},
    {"nama":"Dedi","nilai":70,"kelas":"XI"}
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