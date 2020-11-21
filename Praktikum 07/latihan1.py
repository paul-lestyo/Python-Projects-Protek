path = input("Masukkan nama file : ")

try:
    file = open(path,'r')
    print('isi file',path,'adalah : ',file.read())
except:
    print('file tidak ada/ salah penulisan')