from msvcrt import getch
import getpass
import sys

def pyssword(prompt='Password: '):
    if sys.stdin is not sys.__stdin__:
        pwd = getpass.getpass(prompt)
        return pwd
    else:
        sys.stdout.write(prompt)
        pwd = ""
        while True:
            key = ord(getch())
            if key == 13: #Enter
                sys.stdout.write('\n')
                return pwd
                break
            else:
                char = chr(key)
                sys.stdout.write('*')                
                pwd = pwd + char
