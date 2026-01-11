import datetime
import os

mahasiswa_template = {
    'nama':'nama',
    'nim': '0000',
    'sks_lulus':0,
    'lahir': datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    os.system("cls")

    print(f'{'SELAMAT DATANG':^20}')
    print(f'{'DATA MAHASISWA':^20}')
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())

    mahasiswa['nama'] = input('Nama Mahasiswa : ')
    mahasiswa['nim'] = input('Masukkan Nim : ')
    mahasiswa['sks_lulus'] = input('jumlah sks Lulus : ')
    TAHUN_LAHIR =int(input('Tahun Lahir (yyyy): '))
    BULAN_LAHIR =int(input('Bulan Lahir (1-12): '))
    TANGGAL_LAHIR =int(input('Tanggal Lahir (1-31): '))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    print(mahasiswa)
