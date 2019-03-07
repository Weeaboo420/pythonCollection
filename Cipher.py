import os

#caesar-chiffer
run = True
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " "]
alphabet_up = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " "]

def Clear():
    os.system("cls")

def Encode():
    Clear()

    encode = True
    while encode == True:
        print("---Encode---")
        myText = input("Text to encode>")

        if myText == "":
            pass
        else:
            offset = input("Alphabet offset>")

            if offset == "":
                pass

            else:
                for char in myText:

                    up = False
                    if char.isupper():
                        up = True
                    
                    number = alphabet.index(char.lower()) + int(offset)

                    if number > int(len(alphabet) - 1):

                        if up == False:
                            print(alphabet[int(offset) - 1], end="", flush=True)
                        else:
                            print(alphabet_up[int(offset) - 1], end="", flush=True)

    
                        
                    elif number < int(len(alphabet) - 1):
                        if up == False:
                            print(alphabet[number], end="", flush=True)
                        else:
                            print(alphabet_up[number], end="", flush=True)



                encode = False
                print("")
                print("")
                    
    

def Decode():
    Clear()

    decode = True
    while decode == True:
        print("---Decode---")
        myText = input("Text to decode>")

        if myText == "":
            pass
        else:
            offset = input("Alphabet offset>")

            if offset == "":
                pass

            else:
                for char in myText:


                    up = False
                    if char.isupper():
                        up = True
                        
                    number = alphabet.index(char.lower()) - int(offset)

                    if up == False:
                        print(alphabet[number], end="", flush=True)
                    else:
                        print(alphabet_up[number], end="", flush=True)

                    

                decode = False
                print("")
                print("")


while run == True:
    print("1 - Encode text")
    print("2 - Decode text")
    c = input(">")

    if c == "":
        Clear()

    elif c == "1":
        Encode()

    elif c == "2":
        Decode()

    else:
        Clear()
    
