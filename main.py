import os

def cek_kelulusan(nilai):
    if nilai >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"
    
if not os.path.exists('siswa.txt'):
    print("File siswa.txt tidak ditemukan")
    exit()

if os.path.getsize('siswa.txt') == 0:
    print('file siswa.txt kosong')
    exit()

with open('siswa.txt','r') as file_baca, open('laporan.txt', 'a') as file_tulis:
    for baris in file_baca:
        data = baris.strip().split(',')
        
        nama = data[0]
        nilai = int(data[1])
        
        status = cek_kelulusan(nilai)
        
        print(f'{nama} dengan nilai {nilai} dan status {status}')
        file_tulis.write(f"{nama} - {nilai} - {status}\n")