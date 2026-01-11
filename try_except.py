def cek_umur(teks):
    try:
        umur = int(teks)
    except ValueError:
        return "Input bukan angka"

    if umur >= 18:
        return "Dewasa"
    else:
        return "Belum Dewasa"
cekumur = cek_umur(10)
print(cekumur)