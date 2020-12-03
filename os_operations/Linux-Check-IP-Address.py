# Check public IP Address on Linux

import os

path = r'./plain'
os.system('wget http://ipecho.net/plain')
os.system('clear')

with open(path, 'r') as file:
    line = file.readline()
    print('\nPublic IP Address is: ',line)
    print('\n')

os.system('rm plain')    
#----------------------------
