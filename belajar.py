def simpan_catatan(isi):
    with open('catatan.txt', 'a') as file:
        file.write('\n')
simpan_catatan('sedang belajar')
