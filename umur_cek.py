import datetime as dt
nama = input("Masukkan Nama anda : ")
print(f"Oke {nama}")

print("Silahkan masukkan tanggal, \nbulan dan tahun lahir anda")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir kamu adalah {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini adalah tanggal :{hari_ini}")

#mencari umur
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30


print(f"Ternyata anda sudah :{umur_tahun} tahun {umur_bulan_sisa} bulan")