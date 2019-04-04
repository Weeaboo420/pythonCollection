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
    row1 = ["1", "2", "3"]
    row2 = ["4", "5", "6"]
    row3 = ["7", "8", "*"]

    s1 = symbol(1, 1, fix(row1[0]))
    s2 = symbol(2, 1, fix(row1[1]))
    s3 = symbol(3, 1, fix(row1[2]))

    s4 = symbol(1, 2, fix(row2[0]))
    s5 = symbol(2, 2, fix(row2[1]))
    s6 = symbol(3, 2, fix(row2[2]))

    s7 = symbol(1, 3, fix(row3[0]))
    s8 = symbol(2, 3, fix(row3[1]))
    s9 = symbol(3, 3, fix(row3[2]))


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
    


def scramble():
    s = True

    while s:
        for x in range(30, random.randint(30, 100)):
            r = random.randint(1, 6)

            if r == 1 or r == 2:
                down()
                left()
                left()
                up()
            elif r == 3:
                up()
                right()
                down()
            elif r == 4 or r == 5:
                left()
                left()
                up()
            elif r == 6:
                right()
                down()
                down()
                left()

        if symbols[0].val == "1" and symbols[1].val == "2" and symbols[2].val == "3" and symbols[3].val == "4" and symbols[4].val == "5":
            pass
        else:
            s = False


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

    else:
        pass
        #cannot go any further to the right


generate()
scramble()
clear()
draw()
run = True
while run:
    c = input(">")
    if len(c) == 0:
        pass
    elif c == "up" or c == "w":
        up()
        clear()
        draw()
        
    elif c == "down" or c == "s":
        down()
        clear()
        draw()

    elif c == "left" or c == "a":
        left()
        clear()
        draw()

    elif c == "right" or c == "d":
        right()
        clear()
        draw()
        
    elif c == "new" or c == "reload":
        cleanup()
        clear()
        generate()
        scramble()
        draw()

    else:
        pass
    

