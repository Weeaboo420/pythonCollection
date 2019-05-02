import PIL, os
from PIL import Image

myColor = (66, 244, 173, 255)
pixels, junctions = [], []

class pixel():

    white = False

    def __init__(self, x, y, rgba):
        self.x = x
        self.y = y
        self.rgba = rgba

        if self.rgba == (255, 255, 255, 255):
            self.white = True
        elif self.rgba != (255, 255, 255, 255):
            self.white = False

def find_pixel(x, y):

    for p in pixels:
        if p.x == x and p.y == y:
            return p
        else:
            pass


def find_junctions(width, height):

    start = pixel(0, 0, (0,0,0,0))

    #find the starting pixel which is the first white pixel
    #this method scans from left to right per row of pixels [x, y]: (0, 0) (1, 0) (2, 0)
    #and so on...
    
    for s in pixels:
        if s.y == 0 and s.white == True:
            start.x, start.y, start.rgba = s.x, s.y, s.rgba
        else:
            pass

    print("")
    print(f"Starting pixel: [{start.x}, {start.y}]")
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
                    print(f"NoneType ({a.x}, {a.y})")
                
                elif bottom.white == True:
                    v += 1

            #calculate the final score
            #if there is at least one
            #vertical connection and
            #one horizontal then add
            #this pixel as a junction
            if v >= 1 and h >= 1:
                junctions.append(a)

            
            
        else:
            pass

def scan():
    maze = Image.open("maze.png")

    width, height = maze.width, maze.height
    print(f"Scanning maze.png with a size of ({width}, {height})")
    output = Image.new("RGB", (width, height), 0)


    #scan and add all pixels to a list
    for y in range(0, height):
        for x in range(0, width):

            myPixel = pixel(x, y, maze.getpixel((x,y)))
            pixels.append(myPixel)
            output.putpixel((x, y), maze.getpixel((x, y)))
            
    find_junctions(width, height)

    g = 0
    #compare pixels to junction pixels
    for e in junctions:
            output.putpixel((e.x, e.y), myColor)
            g+= 1
    

    print(f"Pixels: {len(pixels)}, Junction pixels: {g}")
    choice = input("Do you want to save the solution? (y/n) ")


        
    if len(choice) > 0:
        if choice.lower() == "y" or choice.lower() == "yes":

            if os.path.isfile("maze_solved.png"):
                os.remove("maze_solved.png")
            
            output.save("maze_solved.png")
                
        else:
            pass
    else:
        pass

scan()
