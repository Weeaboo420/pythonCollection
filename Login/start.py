#test if the dependencies are installed
try:
    from cryptography.fernet import Fernet
except:
    raise ModuleNotFoundError("Cannot module \'Fernet\' from \'cryptography.fernet\'")    

import program
program.run()