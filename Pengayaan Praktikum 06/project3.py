def dec2Bin(n):
    if(n == 0):
        return "0"
        
    pengali = len(str(n)) - 1
    hasil = 0
    for biner in str(n):
        hasil += 2**pengali * int(biner)
        print(2**pengali, '*', biner)
        pengali -= 1
    return hasil

biner = input("Masukkan biner :")
print('\nangka desimal dari', biner, 'adalah', dec2Bin(biner))
