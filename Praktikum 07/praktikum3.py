import pathlib
path = str(pathlib.Path(__file__).parent)

file = open(path +'/data2.txt')
sum = 0
for data in file:
    try:
        sum += int(data)
    except:
        print( data.rstrip("\n") ,'tidak bisa dikonversikan ke tipe data integer')
print('\nTotal : ' + str(sum))