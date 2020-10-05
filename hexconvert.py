hexDict = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
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

def Convert(hexcode): #Convert from decimal to hex
    decimal = 0    
    currentPower = len(hexcode) - 1   
    
    for char in hexcode:
        decimal += hexDict[str(char)] * (16 ** currentPower)
        currentPower -= 1
    
    return decimal

def UnConvert(decimal): #Convert from hex to decimal
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

    dummy = ""
    hex.reverse()
    return dummy.join(hex)

print("\nWeeaboo\'s HexConverter v1.0")
print("Type \'switch\' to change mode. Type \'exit\' to exit\n")
mode = 0 #0 = to decimal, 1 = to hex

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

        else:
            if mode == 0: #Hex to decimal mode
                canCovert = True
                for char in userInput:
                    if char not in hexDict.keys():
                        canCovert = False
                        break

                if canCovert:
                    print(f"Decimal >> {Convert(userInput)}\n")
                else:
                    print("NaN (Not a number)\n")

            else: #Decimal to hex mode
                print(f"Hex >> {UnConvert(userInput)}\n")
            