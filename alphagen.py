import os, sys, random, time

os.system("cls && color 0B")
ver = "1.0"


def start():

    print("---Alphanumeric Code Generator v", ver,"---")
    print("")
    size = input("Code length? ")

    if size.isdigit():
            generate(int(size))

    else:
        print("")
        print("ERROR - Please enter a valid number")
        print("")
        start()


#universal vars
index = 1
myKey = ""

def generate(sz = 10):


    #global vars
    global index
    global myKey
    
    mySize = sz

    
    alpha_c = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alpha_l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    
    colors = ["9", "A", "B", "C", "D", "E", "F"]
    randomColorNum = random.choice(colors)
    myColor = "0" + randomColorNum
    

    r_select = random.randint(1,3)
    r_char_alpha = random.randint(1, 26)
    r_char_num = random.randint(1, 10)


    if index < (sz + 1):
        if r_select == 1:
            #Capital letters
            myChar = random.choice(alpha_c)

        if r_select == 2:
            #Lowercase letters
            myChar = random.choice(alpha_l)
            
        if r_select == 3:
            #Numbers
            myChar = random.choice(num)


        index += 1
        myKey = myKey + myChar
        generate(mySize)

            
    else:
        print("")
        print(myKey)
        print("")
        print("")


        #nullify obsolete variables
        index = 1
        myKey = ""
        mySize = 0

        os.system("color " + myColor)
        myColor = ""
        
        start()












#init
start()
