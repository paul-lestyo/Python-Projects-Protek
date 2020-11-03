def bin2Dec(s):
    result = ""
    while(s > 1):
        if(s % 2 == 0):
            result = "0" + result
        else:
            result = "1" + result
        s = s//2
    if(s == 1):
        result = "1" + result
    else:
        result = "0" + result
    return result

angka = int(input("Masukkan angka yang ingin dikonversi ke biner : "))
print(bin2Dec(angka))
    