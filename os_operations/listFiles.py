# List files in folder and write their names to lista.txt file

from os import listdir

path = r"E:\folder"
pathFile = "".join([path, r'\lista.txt'])

filenames = [f for f in listdir(path)]

with open(pathFile, 'w') as lista:
    for name in filenames:
        lista.write(name)
        lista.write('\n')
