import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)

try:
    file = open(path + '/data.txt','r')
    bil1 = int(file.readline())
    bil2 = int(file.readline())

    try:
        hasil = bil1/bil2
        print(bil1, 'dibagi',bil2,'sama dengan',hasil)
    except ZeroDivisionError:
        print('tidak boleh pembagian dengan nol')
        
except FileNotFoundError:
    print('file tidak ada')

