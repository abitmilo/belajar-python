matkul = ["Python", "Web", "Database"]


mahasiswa = {
        "nama" : input("masukkan nama: "),
        "semester" : int(input("masukkan semester: ")),
        "status" : input("Status Anda (Aktif/Tidak aktif): ")
}

print(f"Nama mahasiswa : {mahasiswa['nama']}"),
print(f"Semester : {mahasiswa['semester']}"),
print(f"Status : {mahasiswa['status']}")

for pelajaran in matkul:
    print(pelajaran)