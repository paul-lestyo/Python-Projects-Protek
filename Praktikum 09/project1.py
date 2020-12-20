def ubahHuruf(teks, a, b):
    # cara biasa
    listTeks = list(teks)
    result = ""
    for char in listTeks:
        if(char == a):
            char = b
        result = ''.join([result,char])
    return result

    # cara alternatif
    # return teks.replace(a,b)
    

print(ubahHuruf("MATEMATIKA","T","S"))