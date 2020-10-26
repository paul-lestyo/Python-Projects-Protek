from random import randint
count = 1
while True:
    bil = randint(0,10)
    print(bil)
    if bil == 5:
        print("Jumlah perulangan : ", count)
        break
    count += 1