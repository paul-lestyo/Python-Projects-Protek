import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)

file = open(path + '/myfile.txt','r')
print(file.read())