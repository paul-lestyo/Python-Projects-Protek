kodeKar = input("Masukan Kode Karyawan : ")
namaKar = input("Masukan Nama Karyawan : ")
golongan = input("Masukan Golongan     : ")

if(golongan == "A"):
    gajiP = 10000000
    potongan = 2.5

elif(golongan == "B"):
    gajiP = 8500000
    potongan = 2.0
    
elif(golongan == "C"):
    gajiP = 7000000
    potongan = 1.5

elif(golongan == "D"):
    gajiP = 5500000
    potongan = 1.0
else:
    golongan = False
    print("tidak masuk golongan")

if(golongan != False):
    print("\n=======================================")
    print("STRUK RINCIAN GAJI KARYAWAN")
    print("---------------------------------------")
    print("Nama Karyawan      : ",namaKar, " ( Kode:",kodeKar,")")
    print("Golongan           : ", golongan)
    print("---------------------------------------")
    potonganGaji = int(gajiP*potongan/100)
    gajiBersih = gajiP - potonganGaji
    print("Gaji Pokok         : ", gajiP)
    print("Potongan (",potongan,"% ) : ",potonganGaji)
    print("---------------------------------------")
    print("Gaji Bersih        : ", gajiBersih)
