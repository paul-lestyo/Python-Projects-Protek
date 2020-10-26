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
    status = int(input("Masukan Status (1:menikah, 2:blm) : "))
    if(status == 1):
        tunjanganNikah = gajiP * 10/100
        anak = int(input("Masukkan Jumlah Anak : "))
        tunjanganAnak = gajiP * 5/100 * anak
    elif(status == 2):
        tunjanganNikah = 0
        tunjanganAnak = 0
    else:
        print("Input ada yang tidak valid")
        status = False

    if(status != False):
        print("\n=======================================")
        print("STRUK RINCIAN GAJI KARYAWAN")
        print("---------------------------------------")
        print("Nama Karyawan         : ",namaKar, " ( Kode:",kodeKar,")")
        print("Golongan              : ", golongan)

        if(status == 1):
            print("Status                : Menikah")
            print("Jumlah Anak           : ", anak)
        else:
            print("Status                : Belum Menikah")
        
        print("---------------------------------------")
        print("Gaji Pokok            : ", gajiP)
        print("Tunjangan Istri/Suami : ",tunjanganNikah)
        print("Tunjangan Anak        : ",tunjanganAnak)
        print("--------------------------------------- +")
        gajiKotor = gajiP + tunjanganNikah + tunjanganAnak
        print("Gaji Kotor            : ", gajiKotor)
        potonganGaji = int(gajiKotor*potongan/100)
        print("Potongan (",potongan,"% )    : ",potonganGaji)
        print("--------------------------------------- -")
        gajiBersih = gajiKotor - potonganGaji
        print("Gaji Bersih           : ", gajiBersih)

    
