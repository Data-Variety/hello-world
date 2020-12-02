# Check public IP Address on Windows

import os

URL = 'http://ipecho.net/plain'
PATH = r'C:\check\ip.txt'
os.system(f"powershell wget {URL} > {PATH}")

with open(PATH, 'r') as file:
    for line in file:
        if str(line).startswith('Content'):
            IP = line.replace(' ','').replace(':','').replace('Content','Public IP Address is: ')
            print('\n',IP)
            break
#;

os.system(f'del {PATH}')    
#----------------------------
