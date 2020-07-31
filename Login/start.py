#test if the dependencies are installed
from sys import exit
try:
    from cryptography.fernet import Fernet
except:
    print("Module \'cryptography\' could not be found. Use pip to install it. The package can be found at https://pypi.org/project/cryptography/")

import program
program.run()
