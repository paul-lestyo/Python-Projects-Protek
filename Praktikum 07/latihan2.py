path = input("Masukkan nama file : ")

try:
    file = open(path,'r')
    lagi = 'y'
    while lagi == 'y': 
        file = open(path,'a')
        append = input("Data yang mau ditambahkan :")
        file.write(append)
        lagi = input("Mau lagi (y/n)?")
        file.close()
except FileNotFoundError:
    print('file tidak ada/ salah penulisan')
