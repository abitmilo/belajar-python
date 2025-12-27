angkot_awal = int(input("Jumlah Angkot Awal: "))
masuk = int(input("Angkot Masuk: "))
keluar = int(input("Angkot Keluar: "))

angkot_sekarang = angkot_awal + masuk - keluar

if angkot_sekarang < 0 :
    print("ERROR : Angkot melebihi jumlah tersedia")
else : 
    print("Angkot di terminal sekarang ", angkot_sekarang)