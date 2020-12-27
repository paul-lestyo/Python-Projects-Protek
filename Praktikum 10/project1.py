import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)

file = open(path + '/number.txt','r')
ganjil = 0
genap  = 0

for data in file:
    try:
        if(int(data) % 2 == 0):
            ganjil += 1
        else:
            genap += 1
    except:
        print(data.rstrip("\n") ,"bukan angka")
        

print("Banyaknya bilangan genap  :",genap)
print("Banyaknya bilangan ganjil :",ganjil)



        
