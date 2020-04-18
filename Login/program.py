import helpers, os
from getpass import getpass
from enum import Enum
from datetime import datetime, timedelta
from cryptography.fernet import Fernet

functions = []

if not os.path.isfile("db/system.data"):
    keyFile = open("db/system.data", "xb+")
    keyFile.write(Fernet.generate_key())
    keyFile.close()
    
keyFile = open("db/system.data", "rb+")
key = keyFile.readline()
keyFile.close()

registrationLoop = False

class Session:
    def __init__(self, user="NONE"):
        if type(user) is str:
            self.user = user
        else:
            raise TypeError("ERROR: \'user\' has to be of type \'str\'")

session = Session()

class StatusCode(Enum):
    OK = 1
    USERNAME_TAKEN = 2
    INVALID_PASSWORD = 3
    INVALID_USERNAME = 4
    USER_ALREADY_EXISTS = 5
    UNKNOWN_ERROR = 6
    INEXISTENT_DATA = 7

def quit():
    exit()

def IsValidUser(username):
    if os.path.isfile(f"db/users/{username}.data"):
        return StatusCode.USER_ALREADY_EXISTS
    else:
        return StatusCode.OK

def GetPassword(username):
    try:
        userFile = open(f"db/users/{username}.data", "rb")

        f = Fernet(key)                
        token = userFile.readline()
        userFile.close()
        
        token = f.decrypt(token).decode("utf-8")
        return token
    except:
        return StatusCode.UNKNOWN_ERROR

def CreateUser(username, password):
    f = Fernet(key)
    token = f.encrypt(password.encode())

    newUserFile = open(f"db/users/{username}.data", "xb+")
    newUserFile.write(token)
    newUserFile.close()

def GetSession():
    if os.path.isfile("db/session.data"):
        user, span, = None, None
        f = Fernet(key)

        sessionFile = open("db/session.data", "rb+")
        lines = sessionFile.readlines()
        user = f.decrypt(lines[0]).decode("utf-8")
        span = f.decrypt(lines[1]).decode("utf-8")
        span = datetime.strptime(span, '%Y-%m-%d %H:%M:%S.%f')
        return user, span

    else:
        return StatusCode.INEXISTENT_DATA

def SessionIsStillValid():
    if GetSession() != StatusCode.INEXISTENT_DATA:
        data = GetSession()        
        if datetime.now() < data[1]:
            return True
        else:
            return False
    else:
        False

forbiddenChars = []
forbiddenChars.append(" ")
forbiddenChars.append("\'")
forbiddenChars.append("\"")
forbiddenChars.append("´")
forbiddenChars.append("`")
forbiddenChars.append("¨")
forbiddenChars.append("^")
forbiddenChars.append("!")
forbiddenChars.append("¤")
forbiddenChars.append("%")
forbiddenChars.append("&")
forbiddenChars.append("/")

def IsValidInput(inpt):    
    for char in forbiddenChars:
        if char in inpt:
            return False
    return True    

def GetValidChars():
    result = ""
    for char in forbiddenChars:
        if char == forbiddenChars[len(forbiddenChars)-1]:
            result += f"\'{char}\'"
        else:
            result += f"\'{char}\', "
    return result

def CreateSession(username):

    if os.path.isfile("db/session.data"):
        os.remove("db/session.data")

    sessionDuration = datetime.now()
    sessionDuration += timedelta(minutes = 20)
    sessionDuration = str(sessionDuration)
    
    sessionDuration = bytes(sessionDuration, "utf-8")
    username = bytes(username, "utf-8")    

    f = Fernet(key)
    sessionFile = open("db/session.data", "x+")
    sessionFile.close()
    sessionFile = open("db/session.data", "ab+")

    sessionFile.write(f.encrypt(username))
    sessionFile.write(b'\n')
    sessionFile.write(f.encrypt(sessionDuration))
    sessionFile.close()

def logout():
    if session.user != "NONE":
        session.user = "NONE"
    if os.path.isfile("db/session.data"):
        os.remove("db/session.data")
    helpers.clear()

def autologin():
    if SessionIsStillValid():
        data = GetSession()        
        session.user = data[0]
        CreateSession(session.user)
        helpers.clear()

def login():
    if session.user == "NONE":
        loginLoop = True
        username, password = None, None

        step = 1
        msg = ""
        while loginLoop:
            helpers.clear()
            if step != 3:
                print("[Login] Type \'-c to cancel\'")
                print(f"{msg}")
                print("")
                msg = ""

                if step == 2:
                    print(f"Username? {username}")
                    password = getpass("Password? ")

                    if len(password) > 0:
                        if password != "-c":
                            if GetPassword(username) == password and IsValidInput(password):
                                step += 1                        
                            elif GetPassword(username) == StatusCode.UNKNOWN_ERROR:
                                msg = "Something went wrong, make sure you put in the correct password"
                            else:
                                msg = "The passwords do not match"
                        elif password == "-c":
                            helpers.clear()
                            print("[Login cancelled]")
                            loginLoop = False 

                if step == 1:
                    username = input("Username? ")
                    if len(username) > 0:
                        if username != "-c":
                            if IsValidInput(username):
                                if IsValidUser(username) == StatusCode.USER_ALREADY_EXISTS:
                                    step += 1
                                else:
                                    msg = f"\'{username}\' is not a user"
                            else:
                                msg = f"Invalid input, it may not contain {GetValidChars()}"
                            
                        elif username == "-c":
                            helpers.clear()
                            print("[Login cancelled]")                        
                            loginLoop = False                        
            else:
                print("[Login complete]")
                session.user = username
                CreateSession(username)
                loginLoop = False
    else:
        helpers.clear()
        print("You have to log out first.")

def register():    
    registrationLoop = True
    username, password = None, None

    step = 1
    msg = ""
    #steps
    #1 = user name, 2 = password, 3 = done
    while registrationLoop:
        helpers.clear()
        if step != 3:            
            print("[Registration] Type \'-c\' to cancel")
            print(f"{msg}")
            print("")
            msg = ""

            if step == 2:
                print(f"Username? {username}")
                password = getpass("Password? ")
                if len(password) > 0:
                    if password != "-c":
                        step += 1
                    else:
                        helpers.clear()
                        print("[Registration cancelled]")
                        registrationLoop = False

            if step == 1:
                username = input("Username? ")
                if len(username) > 0:
                    if username != "-c":
                        if IsValidUser(username) == StatusCode.OK:
                            step += 1
                        else:
                            msg = "User already exists"
                    else:
                        helpers.clear()
                        print("[Registration cancelled]")
                        registrationLoop = False

        else:
            result = IsValidUser(username)
            
            if result == StatusCode.OK:
                CreateUser(username, password)
                print("[Registration Complete]")

            if result == StatusCode.USER_ALREADY_EXISTS:
                print("[Registration Failed, user already exists]")

            registrationLoop = False


class function:
    def __init__(self, functionReference, aliases = []):
        if callable(functionReference):
            self.functionReference = functionReference
        else:
            raise ValueError("ERROR: Command doesn\'t exist")

        if type(aliases) is list:
            self.aliases = []
            if len(aliases) == 0:                
                self.aliases.append(functionReference.__name__)                
            else:                
                self.aliases.append(functionReference.__name__)
                for alias in aliases:
                    if type(alias) is str:
                        self.aliases.append(alias)                    
        else:
            raise TypeError("ERROR: \'aliases\' is not of type \'list\'")

    def execute(self):
        self.functionReference()


def aliases():
    for func in functions:
        print(f"{func.functionReference.__name__} - ", end="")
        if len(func.aliases) > 0:
            for alias in func.aliases:
                if alias == func.aliases[len(func.aliases)-1]:
                    print(f"{alias} ", end="")
                else:
                    print(f"{alias}, ", end="")
        print("")
    print("")

functions.append(function(register, ["reg"]))
functions.append(function(login, ["lg", "start"]))
functions.append(function(quit, ["exit"]))
functions.append(function(logout, ["out"]))
functions.append(function(aliases, ["al"]))

if not SessionIsStillValid():
    if os.path.isfile("db/session.data"):
        os.remove("db/session.data")
else:
    autologin()

def tryAction(commandName):
    actionExists = False
    for func in functions:        
        for alias in func.aliases:            
            if commandName == alias:
                actionExists = True
                func.execute()
    if not actionExists:
        print(f"The command \"{commandName}\" does not match any existing command")

def main():
    if session.user != "NONE":
        print(f"Logged in as: {session.user}")
    else:
        print("Not currently logged in")

    helpers.showCommands()
    com = input("> ")
    if len(com) > 0:
        tryAction(com)
    else:
        helpers.clear()

def run():
    while True:
        main()