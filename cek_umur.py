umur = int(input("Masukkan umur: "))

if umur >= 0 and umur <= 12:
    print("Kategori: Anak-anak")
elif umur >= 13 and umur <= 17:
    print("Kategori: Remaja")
else:
    print("Kategori: Dewasa")
