import os, sys, random, time


#terminal color
colors = ["A", "B", "C", "D", "E", "F"]
randomColorNum = random.choice(colors)
myColor = "0" + randomColorNum


os.system("cls && color " + myColor)
ver = "1.0"

#universal vars
isGenerating = False

index = 1
myKey = ""
mySize = 0




def start():

    print("---Alphanumeric Code Generator v", ver,"---")
    print("")
    size = input("Code length? ")

    if size.isdigit():
            isGenerating = True
            #print(isGenerating)

            for i in range((int(size) + 1)):
                generate(int(size), isGenerating)

    else:
        print("")
        print("ERROR - Please enter a valid number")
        print("")
        start()



def generate(sz = 10, gen = True):

    global index
    global myKey
    global mySize

    #print("stage 1")

    while gen:
        
        #print("stage 2")

        r_select = 0
        r_char_alpha = 0
        r_char_num = 0

        mySize = sz
        
        alpha_c = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        alpha_l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        

        

        r_select = random.randint(1,3)
        r_char_alpha = random.randint(1, 26)
        r_char_num = random.randint(1, 10)

    
        while (index < (sz + 1)):
        
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
            
            return r_select
            return r_char_alpha
            return r_char_num
            
            #nullify obsolete variables
            print("Here")

                
        while (index == (sz + 1) and gen == True):
            print("")
            print(myKey)
            print("")
            print("")


            #nullify obsolete variables
            index = 1
            myKey = ""
            mySize = 0
            r_select = None
            r_char_alpha = None
            r_char_num = None
            

            gen = False
            start()












#init
start()
