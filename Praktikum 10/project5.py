import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)

file = open(path + '/number2.txt','r')
text = ""

for data in file:
    try:
        angkaAda2 = data.split("|")
        angkaAda2 = angkaAda2
        result = int(angkaAda2[0]) + int(angkaAda2[1].rstrip("\n"))
        text += str(result) + "\n"
    except:
        print(data.rstrip("\n") ,"bukan angka")

resultFile = open(path + '/result.txt','w')
resultFile.write(text)
resultFile.close

        
