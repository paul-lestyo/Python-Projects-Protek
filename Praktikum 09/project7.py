mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']


print("=" * 70)
print("NIM".ljust(10),"NAMA MAHASISWA".ljust(25),"TGL LAHIR".ljust(15),"TEMPAT LAHIR".ljust(15))
print("-" * 70)
for data in mhs:
    dataList = data.split(":")
    nim      = dataList[0]
    nama     = dataList[1]
    
    tglLahir          = dataList[2]
    dataTglLahir      = tglLahir.split('-')
    newFormatTglLahir = "{0}/{1}/{2}".format(dataTglLahir[2],dataTglLahir[1],dataTglLahir[0])

    tmpLahir = dataList[3]

    print(nim.ljust(10),nama.ljust(25),newFormatTglLahir.ljust(15),tmpLahir.ljust(15))

print("=" * 70)