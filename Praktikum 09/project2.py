def bintang(n):
    for x in range(1,n):
        bintangs = "*" * (1 +(x-1)*2)
        print(bintangs.center(1+2*n))

bintang(5)