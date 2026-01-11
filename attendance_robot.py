import os

os.system('cls')
# #tugas 1
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(f"Bilangan {i} adalah Genap")
#     else:
#         print(f"Bilangan {i} adalah ganjil")


#tugas 2        
password_benar = "python1234"

while True:
        input_user = input("Masukkan password ")
    
        if input_user == password_benar:
            print("Login Berhasil! Selamat datang")
            break
        else:
            print("Password salah! Coba lagi")
        
print("Program Selesai")