import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)

teks = "SAYA SUKA PYTHON"

caesar = int(input("masukan n sandi caesar :"))
listTeks = list(teks)

result = ""
for charTeks in listTeks:
    if(charTeks.isalpha()):
        hurufAscii  = ord(charTeks)
        indexAplha  = hurufAscii - ord("A")
        newIndex    = (indexAplha + caesar) % 26
        newCaesar   = newIndex + ord("A")
        newChar     = chr(newCaesar)
        result += newChar 
    else:
        result += charTeks
    
    
resultFile = open(path + '/resultEncodeCaesar.txt','w')
resultFile.write(result)
resultFile.close