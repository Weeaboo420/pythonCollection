import os, time, sys
#vars
run = True

rowList = []

os.system("color 0B")
print("Scrito Text Editor")


def Flash():

    i = 0
    while i < 4: 
        os.system("color 0D")
        time.sleep(0.02)
        os.system("color 0B")
        time.sleep(0.02)
        i += 1



while run == True:

    content = input(">")

    if content == "-s":

        try:
            fname = input("Full filename? ")
            f = open(str(fname), "x")

            for line in rowList:
            
                f.write(line + "\n")

            f.close()
            print("File created")
            Flash()
            input("Press ENTER to continue...")
            rowList.clear()
            os.system("cls")
            print("-New File-")
            
        except:
            print("Error: Empty content or invalid filename. Maybe the file already exists?")
            Flash()


    elif content == "-q":
        sys.exit()

    elif content == "-r":
        rname = input("Filename to remove? ")

        try:
            Flash()
            os.remove(str(rname))
            time.sleep(1)
            print("File removed")
            Flash()
            time.sleep(2)
            rowList.clear()
            os.system("cls")
            print("-New File-")

        except:
            print("Error: File does not exist or invalid filename")
            Flash()
            time.sleep(2)
            os.system("cls")

    else:
        rowList.append(str(content))
    
        
        
