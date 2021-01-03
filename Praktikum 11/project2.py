import pathlib
from datetime import datetime,timedelta
path = current_dir = str(pathlib.Path(__file__).parent)

def getTglKembali(now):
    return now + timedelta(days=7)

lagi = 'y'
text = ""

while lagi=="y":
    kode  = input("Masukkan Kode Member : ")
    nama  = input("Masukkan Nama Member : ")
    judul = input("Masukkan Judul Buku  : ")

    now = datetime.date(datetime.now())
    text += "{0}|{1}|{2}|{3}|{4}\n".format(kode,nama,judul,now,getTglKembali(now))
    lagi = input("Ulangi lagi (y/n)  :")


resultFile = open(path + '/resultPeminjaman.txt','w')
resultFile.write(text)
resultFile.close