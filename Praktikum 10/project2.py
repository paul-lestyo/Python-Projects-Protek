import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)

file = open(path + '/biodata.txt','w')

lagi = "y"
while (lagi == "y"):
    nim    = input("Masukkan NIM    :")
    nama   = input("Masukkan Nama   :")
    alamat = input("Masukkan Alamat :")

    file.write("{0}|{1}|{2}\n".format(nim,nama,alamat))

    lagi = input("ingin input lagi (y/n)  :")

file.close

