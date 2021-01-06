# getpwd

![PyPI](https://img.shields.io/pypi/v/getpwd)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/getpwd)
![PyPI - Platform](https://img.shields.io/badge/Platform-Windows%7CLinux-green)


Python tool to get a password from the user and display a masked value at the prompt.

## Installing
```pip install getpwd```

## Using
```Python
>>> from getpwd import getpwd
>>> secret = getpwd()
Password: ********
>>> print(secret)
mysecret
```


If you would like to make any comments then please feel free to email me at rafael.alves.ribeiro@gmail.com



