def getAverage(data):
    tupleData = tuple(data.values())
    sumData = sum(tupleData)
    count = len(tupleData)
    return sumData/count

    



buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
result = getAverage(buah)
if(result):
    print("Buah yang harga satuannya paling mahal yaitu {0} dengan harga {1}".format(result,buah[result]))

