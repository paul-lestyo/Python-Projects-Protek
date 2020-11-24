def dataStat(x):
    if(isinstance(x, list)):
        tupleX  = tuple(x)
        a  = sum(tupleX) / len(tupleX)
        b  = max(tupleX) 
        c  = min(tupleX)

        return [a, b, c]
    else:
        print('Data yang dimasukkan bukan bertipe data list')
        return False

def getListFromUser():
    try:
        count = int(input('ingin memasukkan berapa angka? '))
        loop = 0
        data = []
        while loop < count:
            number = int(input("Masukkan bilangan bulat ke-{0} : ".format(loop+1)))
            data.append(number)
            loop += 1

        return data
    except ValueError:
        print('data yang anda masukan bukan angka / salah')
        return False



dataList = getListFromUser()
if(dataList):
    result   = dataStat(dataList)
    print("\nRata-rata dari list {0}        : {1}".format(dataList,result[0]))
    print("\nNilai tertinggi dari list {0}  : {1}".format(dataList,result[1]))
    print("\nNilai terendah dari list {0}   : {1}".format(dataList,result[2]))


