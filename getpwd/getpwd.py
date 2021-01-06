import getpass
import os
import sys

if os.name == "nt":
    from msvcrt import getch
else:
    from readchar import readchar as getch


is_windows = os.name == "nt"
is_linux = os.name == "posix"

BACKSPACE_WINDOWS = 8
BACKSPACE_LINUX = 127
RETURN_KEY = 13


def getpwd(prompt: str = "Password: ") -> str:
    """
    Prompt for a password and masks the input.
    Returns:
        the value entered by the user.
    """

    if sys.stdin is not sys.__stdin__:
        pwd = getpass.getpass(prompt)
        return pwd
    else:
        pwd = ""
        sys.stdout.write(prompt)
        sys.stdout.flush()
        while True:
            key = ord(getch())
            if key == RETURN_KEY:
                sys.stdout.write("\n")
                return pwd
                break
            if (
                is_windows
                and key == BACKSPACE_WINDOWS
                or is_linux
                and key == BACKSPACE_LINUX
            ):
                if len(pwd) > 0:
                    # Erases previous character.
                    sys.stdout.write("\b" + " " + "\b")
                    sys.stdout.flush()
                    pwd = pwd[:-1]
            else:
                # Masks user input.
                char = chr(key)
                sys.stdout.write("*")
                sys.stdout.flush()
                pwd = pwd + char
