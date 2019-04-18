import os
ver = "1.0 (April 18th 2019)"

print(f"cif (Command-InterFace) v{ver}")

def show_files(ex):
    
    files = []
    ext = "." + str(ex)

    for f in os.listdir(os.getcwd()):
        if f.endswith(ext):
            files.append(f)
        else:
            pass

    dirList = []
    allFiles = []
    for f in os.listdir(os.getcwd()):
        allFiles.append(f)

    #print(allFiles)
    
    if ex == " ":

        #dirName = ""
        for element in allFiles:
            if "." in element:
                pass
            else:
                dirList.append(element)

            #for char in element:

            #    a = True
            #    if char == ".":
            #        dirName = ""
            #        a = False
                    
            #    else:
            #        if a == True:
            #            dirName += char
            #        else:
            #            pass

            #    if len(dirName) == len(element) and a == True:
            #        dirList.append(dirName)

        for element in dirList:
            print(element)

    else:    
        for file in files:
            print(file)


def interpret(i):
    arguments = []

    word = ""
    i += " "

    quote = False
    for char in i:
        if char == '"' and quote == False:
            quote = True
            
        elif char == '"' and quote == True:
            quote = False
        
        elif char == " ":
            if quote == True:
                word += char
            
            else:
                arguments.append(word)
                word = ""
        else:
            word += char

    #print(arguments)

    if arguments[0] == "ls" and len(arguments) >= 3 and arguments[1] == "-t" :

        ext = []
        for x in range(0, len(arguments)):
            if x > 0:
                ext.append(arguments[x])

            else:
                pass

        #print("Formats: ", end="")
        #for x in range(0, len(ext)):
        #    if x < len(ext)-1:
        #        print(ext[x], end=", ")
        #    else:
        #        print(ext[x], end="")

        #print("")

        for extension in ext:
            #line = "List of " + str(extension) 
            #print(line)

            #for x in range(0, len(line)):
            #    print("-", end="")
            show_files(extension)
            print("")

    elif arguments[0] == "ls" and len(arguments) == 2 and arguments[1] == "-d":
        show_files(" ")
        print("")
    
    elif arguments[0] == "cd" and len(arguments) == 2:
        try:
            os.chdir(arguments[1])
        except:
            pass

    elif arguments[0] == "ls" and len(arguments) == 1:

        p = os.path.basename(os.getcwd())
    
        if len(p) > 0:    
            print(f"Showing contents of {p}")
        else:
            print(f"Showing contents of {os.getcwd()}")
        
        print("")
        for element in os.listdir(os.getcwd()):
            print(element)
        print("")

    elif arguments[0] == "clear" or arguments[0] == "cls":
        if len(arguments) == 1:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
        else:
            pass
        
while True:
    c = input(f"{os.getcwd()}>")

    if len(c) == 0:
        pass
    else:
        interpret(c)
