def isPrime(x):
    if(x == 1 or x < 1):
        print('Angka adalah angka satu atau bukan bilangan asli')
        return False
    print("Apakah angka",str(x), "adalah bilangan prima?")
    pembagi = x - 1
    print("Prosedur Pengecekan :\n")
    while(pembagi > 1):
        print(str(pembagi), "membagi habis", str(x),"?",end='')
        if(x%pembagi == 0):
            print(" True")
            return False
        print(" False")
        pembagi -= 1
    
    return True

angka = int(input("Masukkan Angka: "))
hasil = "Bukan Prima"

if(isPrime(angka)):
    hasil = "Prima"

print("Kesimpulan : ",angka, hasil)

    
