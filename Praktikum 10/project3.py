import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)

file = open(path + '/biodata.txt','r')

dataMhs = {}

i = 1
for data in file:
    dictsiji = {}
    dataDict = data.split("|")
    dictsiji['nim'] = dataDict[0]
    dictsiji['nama'] = dataDict[1]
    dictsiji['tempat'] = dataDict[2].rstrip("\n")

    dataMhs[i] = dictsiji
    i += 1

print(dataMhs)


    