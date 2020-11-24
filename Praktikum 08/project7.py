def sortFromExpensive(data):
    listData = list(data.values())
    listData.sort(reverse=True)
    for x,y in data.items():
        if(listData[0] == y):
            return x
    return False



buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
result = sortFromExpensive(buah)
if(result):
    print("Buah yang harga satuannya paling mahal yaitu {0} dengan harga {1}".format(result,buah[result]))

