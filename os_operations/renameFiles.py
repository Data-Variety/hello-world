# Rename "jpg" files in directory to numbers

from os import listdir, rename

path = r"C:\Photo"

filenames = [f for f in listdir(path) if f[-4:] == '.jpg']
count = len(filenames) + 1

newFilenames = [str(i) + '{}'.format(".jpg") for i in range(1,count)]

z = zip(filenames,newFilenames)

d = dict(z)

for file in listdir(path):
    if file in d.keys():
        rename(path + "\\" + file, path + "\\" + d[file])
