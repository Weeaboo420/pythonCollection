import os, random
symbols = []


class symbol:

    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def fix(i):
    p1 = i.rstrip()
    p2 = p1.lstrip()
    return p2

def generate():

    global symbols
    defSymbols = ["1", "2", "3", "4", "5", "6", "7", "8", "*"]

    c1 = defSymbols[random.randint(0, len(defSymbols)-1)]
    s1 = symbol(1, 1, fix(c1))
    defSymbols.remove(c1)

    c2 = defSymbols[random.randint(0, len(defSymbols)-1)]
    s2 = symbol(2, 1, fix(c2))
    defSymbols.remove(c2)

    c3 = defSymbols[random.randint(0, len(defSymbols)-1)]
    s3 = symbol(3, 1, fix(c3))
    defSymbols.remove(c3)



    c4 = defSymbols[random.randint(0, len(defSymbols)-1)]
    s4 = symbol(1, 2, fix(c4))
    defSymbols.remove(c4)

    c5 = defSymbols[random.randint(0, len(defSymbols)-1)]
    s5 = symbol(2, 2, fix(c5))
    defSymbols.remove(c5)

    c6 = defSymbols[random.randint(0, len(defSymbols)-1)]
    s6 = symbol(3, 2, fix(c6))
    defSymbols.remove(c6)



    c7 = defSymbols[random.randint(0, len(defSymbols)-1)]
    s7 = symbol(1, 3, fix(c7))
    defSymbols.remove(c7)

    c8 = defSymbols[random.randint(0, len(defSymbols)-1)]
    s8 = symbol(2, 3, fix(c8))
    defSymbols.remove(c8)

    c9 = defSymbols[random.randint(0, len(defSymbols)-1)]
    s9 = symbol(3, 3, fix(c9))
    defSymbols.remove(c9)


    symbols.append(s1)
    symbols.append(s2)
    symbols.append(s3)

    symbols.append(s4)
    symbols.append(s5)
    symbols.append(s6)

    symbols.append(s7)
    symbols.append(s8)
    symbols.append(s9)


def cleanup():
    global symbols
    symbols.clear()
    



def p(element, element2, element3):

    #global symbols
    print(f"  {element.val}   {element2.val}   {element3.val}")
    print("")


def draw():
    print("")
    #p(s1, s2, s3)
    #p(s4, s5, s6)
    #p(s7, s8, s9)
    print(f"  {symbols[0].val}   {symbols[1].val}   {symbols[2].val}")
    print("")
    print(f"  {symbols[3].val}   {symbols[4].val}   {symbols[5].val}")
    print("")
    print(f"  {symbols[6].val}   {symbols[7].val}   {symbols[8].val}")
    print("")

def getPos():
    xPos = 0
    yPos = 0
    for element in symbols:
        if element.val == "*":
            xPos = element.x
            yPos = element.y
        else:
            pass

    return xPos, yPos

def find(x, y):
    xPos = 0
    yPos = 0
 
    for element in symbols:
        if element.x == x and element.y == y:
            return element
        else:
            pass


def up():
    x, y = getPos()

    if y > 1:
        newBlock = find(x, y-1)
        myBlock = find(x, y)

        myBlock.val = newBlock.val
        newBlock.val = "*"
        clear()
        draw()

    else:
        pass
        #cannot go higher


def down():
    x, y = getPos()

    if y < 3:
        newBlock = find(x, y+1)
        myBlock = find(x, y)

        myBlock.val = newBlock.val
        newBlock.val = "*"
        clear()
        draw()

    else:
        pass
        #cannot go lower


def left():
    x, y = getPos()

    if x > 1:
        newBlock = find(x-1, y)
        myBlock = find(x, y)

        myBlock.val = newBlock.val
        newBlock.val = "*"
        clear()
        draw()

    else:
        pass
        #cannot go any further to the left


def right():
    x, y = getPos()

    if x < 3:
        newBlock = find(x+1, y)
        myBlock = find(x, y)

        myBlock.val = newBlock.val
        newBlock.val = "*"
        clear()
        draw()

    else:
        pass
        #cannot go any further to the right


generate()
draw()
run = True
while run:
    c = input(">")
    if len(c) == 0:
        pass
    elif c == "up" or c == "w":
        up()
        
    elif c == "down" or c == "s":
        down()

    elif c == "left" or c == "a":
        left()

    elif c == "right" or c == "d":
        right()
        
    elif c == "new" or c == "reload":
        cleanup()
        clear()
        generate()
        draw()

    else:
        pass
    

