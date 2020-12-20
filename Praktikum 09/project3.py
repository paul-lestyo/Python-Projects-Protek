def starFormation1(z,n):
    for x in range(1,n+1):
        bintangs = "*" * (1 +(x-1)*2)
        print(bintangs.center(1+2*z))

def starFormation2(z,n):
    for x in range(n,0,-1):
        bintangs = "*" * (1 +(x-1)*2)
        print(bintangs.center(1+2*z))

def starFormation3(n):
    if(n % 2 == 1): 
        # Jika Ganjil
        starFormation1(n, n//2 + 1)
        starFormation2(n, n//2)
    else:
        print("bilangan harus ganjil")


baris = int(input("Masukan baris bintang : "))
starFormation3(baris)