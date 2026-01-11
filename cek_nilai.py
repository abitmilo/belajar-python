siswa = [
    {"nama":"andi","nilai": 90},
    {"nama":"budi","nilai": 63},
    {"nama":"cici","nilai": 89}
]

def cek_grade(nilai):
    if nilai >= 85 <= 100:
        return "A"
    elif nilai >= 75 <= 84:
        return "B"
    elif nilai >= 0 <= 74 :
        return "C"
    else:
        return "Nilai Tidak Terbaca Sistem"
    
for s in siswa:
    grade = cek_grade(s["nilai"])
    print(f"{s["nama"]}, "-", {grade}")