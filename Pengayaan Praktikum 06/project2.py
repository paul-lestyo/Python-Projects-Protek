def sqNumbers(a,b):
    sequence = 1
    while(sequence**2 < b):
        if(sequence**2 > a):
            print(sequence**2,end=' ')
        sequence += 1


awal = int(input("Masukkan range angka kuadrat awal :"))
akhir = int(input("Masukkan range angka kuadrat akhir :"))
sqNumbers(awal,akhir)
