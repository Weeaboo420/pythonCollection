hexDict = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

decimalDict = {
    "10": "A",
    "11": "B",
    "12": "C",
    "13": "D",
    "14": "E",
    "15": "F"
}

def HexToDecimal(hexcode): #Convert from hex to decimal
    decimal = 0    
    currentPower = len(hexcode) - 1   
    
    for char in hexcode:
        if str(char) not in hexDict.keys() and int(char) <= 9:
            decimal += int(char) * (16 ** currentPower)
        else:
            decimal += hexDict[str(char)] * (16 ** currentPower)
        currentPower -= 1
    
    return decimal

def DecimalToHex(decimal): #Convert from decimal to hex
    hex = []
    decimal = str(decimal)

    nextNum = int(decimal)

    for num in decimal:
        remainder = nextNum % 16
        nextNum = int(nextNum / 16)
        
        if remainder < 10:
            hex.append(str(remainder))
        else:
            hex.append(decimalDict[str(remainder)])

    if hex[len(hex)-1] == "0":
        hex.pop()
    
    hex.reverse()    
    prefix = ""
    if fullHexMode:
        prefix = "0x"

    if len(prefix) > 0:
        hex.insert(0, prefix)
    
    return "".join(hex)
    

print("\nWeeaboo\'s HexConverter v1.0")
print("Type \'switch\' to change mode. Type \'exit\' to exit")
print("Type \'toggle-hex\' to toggle hex code display\n")
mode = 0 #0 = to decimal, 1 = to hex
fullHexMode = False #Should hex codes have a "0x" before them or not when converting from decimal to hex?

while True:
    if mode == 0:
        print("Hex-to-Decimal > ", end="")
    else:
        print("Decimal-to-Hex > ", end="")

    userInput = input("")
    userInput = userInput.upper()

    if len(userInput) > 0:
        if userInput.lower() == "exit":
            exit()
        
        elif userInput.lower() == "switch": #Switch conversion mode
            if mode == 0:
                mode = 1                
            else:
                mode = 0
        
        elif userInput.lower() == "toggle-hex":
            fullHexMode = not fullHexMode
            print("Hex display toggled")

        else:
            if len(userInput) >= 2 and userInput[0].lower() == "0" and userInput[1].lower() == "x":
                newUserInput = ""
                for i, char in enumerate(userInput):
                    if i > 1:
                        newUserInput += char
                userInput = newUserInput

            canConvert = True
            errorMessage = ""

            for char in userInput:

                if mode == 0 and canConvert:
                    if char not in hexDict.keys():
                        try:
                            int(char)
                            if int(char) < 0:
                                canConvert = False
                                errorMessage = "Negative numbers not allowed"
                                break
                        except:                                              
                            canConvert = False
                            errorMessage = f"Can\'t convert hex \'{userInput}\' to decimal"
                            break
                                        

            if mode == 0: #Hex to decimal mode
                if canConvert:
                    print(f"Decimal >> {HexToDecimal(userInput)}\n")
                else:
                    print(f"{errorMessage}\n")

            else: #Decimal to hex mode
                if canConvert:
                    print(f"Hex >> {DecimalToHex(userInput)}\n")
                else:
                    print("NaN (Not a number)\n")