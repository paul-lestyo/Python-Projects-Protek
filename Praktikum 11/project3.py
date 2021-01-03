import pathlib
from datetime import datetime,timedelta
path = current_dir = str(pathlib.Path(__file__).parent)

def getTerlambat(x):
    now = datetime.date(datetime.now())
    x = datetime.strptime(x, "%Y-%m-%d").date()
    return int((now - x).days)


search = input("Masukan Kode Member : ")

file = open(path + '/resultPeminjaman.txt','r')

result = False

for data in file:
    data_copy = data.split("|").copy()
    kode = data.split("|")[0]
    if(kode == search):
        result = data_copy
        break
        


if(result):
    maksPinjam = result[4].rstrip('\n')
    terlambat = getTerlambat(maksPinjam)

    if(terlambat <= 0):
        textTerlambat = "Tidak Terlambat"
        denda         = "Tidak Ada Denda"
    elif(terlambat > 0):
        textTerlambat = str(terlambat) + " hari"
        denda         = "Rp " + str(terlambat*2000)

    print("Data Peminjaman Buku")
    print("Kode Member                 : ", result[0])
    print("Nama Member                 : ", result[1])
    print("Judul Buku                  : ", result[2])
    print("Tanggal Mulai Peminjaman    : ", result[3])
    print("Tanggal Maks Peminjaman     : ", maksPinjam)
    print("Tanggal Pengembalian        : ", datetime.date(datetime.now()))
    print("Terlambat                   : ", textTerlambat)
    print("Denda                       : ", denda)
else:
    print("Data mahasiswa tidak ditemukan")