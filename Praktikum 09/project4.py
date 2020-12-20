import random
def shuffleString(x, n):
    listResult = []
    i = 0
    while i < n:
        acak = ''.join(random.sample(x,len(x)))
        if(acak not in listResult):
            listResult += [acak]
            i += 1
    print(listResult)

    

shuffleString('aku',2)
shuffleString('aku',3)
shuffleString('aku',4)