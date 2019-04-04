import os

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


s1 = symbol(1, 1, "1")
s2 = symbol(2, 1, "7")
s3 = symbol(3, 1, "3")

s4 = symbol(1, 2, "4")
s5 = symbol(2, 2, "*")
s6 = symbol(3, 2, "6")

s7 = symbol(1, 3, "2")
s8 = symbol(2, 3, "8")
s9 = symbol(3, 3, "5")

symbols = []

symbols.append(s1)
symbols.append(s2)
symbols.append(s3)

symbols.append(s4)
symbols.append(s5)
symbols.append(s6)

symbols.append(s7)
symbols.append(s8)
symbols.append(s9)


def p(element, element2, element3):

    global symbols
    print(f"  {element.val}   {element2.val}   {element3.val}")
    print("")


def draw():
    print("")
    p(s1, s2, s3)
    p(s4, s5, s6)
    p(s7, s8, s9)


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



draw()
run = True
while run:
    c = input(">")
    if len(c) == 0:
        pass
    elif c == "up" or c == "u":
        up()
        
    elif c == "down" or c == "d":
        down()

    elif c == "left" or c == "l":
        left()

    elif c == "right" or c == "r":
        right()
        
    else:
        pass
    

