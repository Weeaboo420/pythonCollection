import PIL, os, sys
from PIL import Image

 

class pixel():
    def __init__(self, x, y, rgba):
        self.x = x
        self.y = y
        self.rgba = rgba
        self.white = False
        if self.rgba == (255, 255, 255, 255) or self.rgba == (255, 255, 255):
            self.white = True

#vars   
green = (107, 255, 179, 255)
red = (255, 79, 79, 255)
blue = (66, 135, 245, 255)
purple = (163, 4, 207, 255)
special = (85, 84, 125, 255)

dark_mode = False

pixels, reds, junctions = [], [], []
start, goal = pixel(0, 0, (0,0,0,0)), pixel(0, 0, (0,0,0,0))
argv = sys.argv

if len(argv) == 2:
    if argv[1].lower() == "-dark" or argv[1].lower() == "-darkmode" or argv[1].lower() == "-dark_mode":
        dark_mode = True
       

def find_pixel(x, y):
    for p in pixels:
        if p.x == x and p.y == y:
            return p
        else:
            pass

def find_junctions(width, height):    
    #find the starting pixel which is the first white pixel
    #this method scans from left to right per row of pixels [x, y]: (0, 0) (1, 0) (2, 0)
    #and so on...
    for s in pixels:
        if s.y == 0 and s.x > 0 and s.white:
            start.x, start.y, start.rgba = s.x, s.y, s.rgba
        if s.y == height - 1 and s.white:
            goal.x, goal.y, goal.rgba = s.x, s.y, s.rgba
        else:
            pass

    print("")    
    print("Calculating junctions...")

    #find junctions
    for a in pixels:
        if a.white == True:
            h = 0
            v = 0
            #horizontal
            if a.x > 0:
                left = find_pixel(a.x-1, a.y)
                if left.white == True:
                    h += 1

            if a.x < width:
                right = find_pixel(a.x+1, a.y)
                if right.white == True:
                    h += 1

            #vertical
            if a.y > 0:
                top = find_pixel(a.x, a.y-1)
                if top.white == True:
                    v += 1

            if a.y < height and a.y > 0:
                bottom = find_pixel(a.x, a.y+1)

                if bottom is None:
                    print(f"({a.x}, {a.y})")
                elif bottom.white == True:
                    v += 1

            #calculate the final score
            #if there is at least one
            #vertical connection and
            #one horizontal then add
            #this pixel as a junction
            if v >= 1 and h >= 1:
                junctions.append(a)

            elif v == 1 and h == 0 and a.y != (height-1):
                reds.append(a)                

            elif h == 1 and v == 0:
                reds.append(a)
        else:
            pass        

def scan():
    maze = Image.open("maze.png")
    width, height = maze.width, maze.height    
    
    if os.path.isfile("maze_enlarged.png"):
        os.remove("maze_enlarged.png")    

    maze_enlarged = maze.resize((width*100, height*100), PIL.Image.NEAREST)
    maze_enlarged.save("maze_enlarged.png")

    print(f"Scanning maze.png with a size of ({width}, {height})")
    output = Image.new("RGB", (width, height), 0)
    if dark_mode:
        print("[dark mode enabled]")

    #scan and add all pixels to a list
    for y in range(0, height):
        for x in range(0, width):
            myPixel = pixel(x, y, maze.getpixel((x,y)))
            pixels.append(myPixel)
            if not dark_mode:
                output.putpixel((x, y), maze.getpixel((x, y)))
            else:
                darkerColor = maze.getpixel((x, y))
                if darkerColor[0] == 255 and darkerColor[1] == 255 and darkerColor[2] == 255:
                    darkerColor = special
                output.putpixel((x, y), darkerColor)

    find_junctions(width, height)            
    junction_count = 0
    #compare pixels to junction pixels
    for j in junctions:
        output.putpixel((j.x, j.y), green)
        junction_count += 1

    dead_count = 0
    for d in reds:
        output.putpixel((d.x, d.y), red)
        dead_count += 1

    output.putpixel((start.x, start.y), blue)
    output.putpixel((goal.x, goal.y), purple)

    print(f"Pixels: {len(pixels)}, Junction pixels: {junction_count}, Dead ends: {dead_count}")
    choice = input("Do you want to save the solution? (y/n) ")

    if len(choice) > 0:
        if choice.lower() == "y" or choice.lower() == "yes":
        
            if os.path.isfile("maze_solved.png"):
                os.remove("maze_solved.png")
            sized_output = output.resize((width*100, height*100), PIL.Image.NEAREST)
            sized_output.save("maze_solved.png")
        else:
            pass
    else:
        pass

scan()
