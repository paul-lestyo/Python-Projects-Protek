import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)


search = input("Masukan NIM yang ingin dicari : ")

file = open(path + '/biodata.txt','r')

result = False

for data in file:
    data_copy = data.split("|").copy()
    nim = data.split("|")[0]
    if(nim == search):
        result = data_copy
        break
        

if(result):
    print("Data Mahasiswa")
    print("NIM         :", result[0])
    print("Nama        :", result[1])
    print("Alamat      :", result[2])
else:
    print("Data mahasiswa tidak ditemukan")