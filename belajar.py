

with open('siswa.txt', 'w') as file:
    nama = input('Masukkan nama : ')
    kelas = input('Kelas : ')
    hobi = input('Hobi : ')
    file.write(f'nama {nama} kelas {kelas} hobi {hobi}')
    print(f'Nama kamu adalah {nama} dan kamu kelas {kelas} kamu mempunyai hobi {hobi}')
