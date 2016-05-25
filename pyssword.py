from msvcrt import getch
import getpass, sys
import time

def pyssword(prompt='Password: '):
    '''
        Prompt for a password and masks the input.
        Returns:
            the value entered by the user.
    '''
    
    if sys.stdin is not sys.__stdin__:
        pwd = getpass.getpass(prompt)
        return pwd
    else:
        pwd = ""
        print len(pwd)
        countBackSpace = 0
        sys.stdout.write(prompt)        
        while True:
            key = ord(getch())
            if key == 13: #Return Key
                sys.stdout.write('\n')
                return pwd
                break
            if key == 8: #Backspace key
                if len(pwd) > 0:
                    # Erases previous character.
                    sys.stdout.write('\b' + ' ' + '\b')                
                    sys.stdout.flush()
                    pwd = pwd[:-1]                    
            else:
                # Masks user input.
                char = chr(key)
                sys.stdout.write('*')                
                pwd = pwd + char            
