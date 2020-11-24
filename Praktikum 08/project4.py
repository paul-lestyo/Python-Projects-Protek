data = ["bayam", "kangkung", "wortel", "selada"]
print('=' * 30)
print('Mengolah Data-Data Sayur')
print('=' * 30)

lagi = 'y'
while lagi == 'y':

    print("A. Tambah data sayur")
    print("B. Hapus data sayur")
    print("C. Tampilkan data sayur\n")

    choose = input("Pilihan Anda : ")
    if(choose.lower() == 'a'):
        append = input('data sayur yang ingin dimasukkan : ')
        data.append(append)

    elif(choose.lower() == 'b'):
        delete = input('data sayur yang ingin dihapus : ')
        try:
            data.remove(delete)
            print('{0} berhasil dihapus'.format(delete))
        except ValueError:
            print('{0} tidak ada dalam data\n'.format(delete))

    elif(choose.lower() == 'c'):
        print("data sayur : {0}\n".format(data))
    else:
        print('tidak ada pilihan {0}\n'.format(choose))

    lagi = input('ingin mengolah data lagi (y/n)? ')