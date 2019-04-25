from PIL import Image
import os, random as ran, os


def generate(size_x, size_y, shade):

    myImage = Image.new("RGB", (size_x, size_y), 0)
    myName = "image_"
    i = 0
    myName += str(i)
    
    #myName += str(ran.randrange(100000, 10000000, ran.randint(1, 10)))
    myName += ".jpg"

    resX, resY = myImage.size
    print(f"RGB-Shade: {shade}")
    e = False

    for y in range(resY):
        for x in range(resX):
            #s = x+y
            #myImage.putpixel((x, y), (ran.randrange(0, 255), ran.randrange(0, 255), ran.randrange(0, 255)))

            rS, gS, bS = "", "", ""
            seq = 1

            
            for val in shade:
                if val.isdigit():

                    if seq == 1:
                        rS += val

                    elif seq == 2:
                        gS += val

                    elif seq == 3:
                        bS += val
                        
                elif val == ",":
                    seq += 1

                elif val == " ":
                    pass

                else:
                    pass
            
            r, g, b = int(rS), int(gS), int(bS)

            if r <= 255 and r >= 0 and g <= 255 and g >= 0 and b <= 255 and b >= 0:
                new_r = round(round(ran.uniform(0, 1), 3) * r)
                new_g = round(round(ran.uniform(0, 1), 3) * g) 
                new_b = round(round(ran.uniform(0, 1), 3) * b) 

                myImage.putpixel((x, y), (new_r, new_g, new_b))

                
            else:
                if e == False:
                    e = True
                else:
                    pass
        
            #if s % 2 == 0:
            #    myImage.putpixel((x, y), (255, 255, 255))
            #else:
            #    myImage.putpixel((x, y), 0)

    if e == True:
        print("ERROR: RGB values range from 0 to 255")
    elif e == False:

        while os.path.isfile(myName):
            myName = "image_"
            i += 1
            myName += str(i)
            myName += ".jpg"
            
        myImage.save(myName, "jpeg")
        print(f"Saved image as {myName} ({resX}x{resY})")


#while True:
def run(size, rgb):

    #mySize = input("Image size (*x*)? ")
    mySize = len(size)

    if mySize >= 4:
        if "x" in size:

            my_X = ""
            my_Y = ""
            p2 = False
            
            for char in size:

                if p2 == False:
                    if char == "x":
                        p2 = True
                    else:
                        my_X += char

                elif p2 == True:
                    my_Y += char

            if my_X.isdigit() and my_Y.isdigit():

                #s = input("Shade RGB (r, g, b)? ")
                s = rgb
                if len(s) > 0:
                    if "(" in s and ")" in s and "," in s and "," in s:
                        #print("There is a tuple")
                        #print(f"s: {s}")
                        generate(int(my_X), int(my_Y), rgb)

                        
                    else:
                        print("Expected an RGB tuple. Example: (255, 255, 255)")
                else:
                    pass
                
                    
            else:
                print("Try again")
        
        else:
            print("An x is needed in your input, example: 640x480")
        
    else:
        print("Invalid size or too small dimensions")

    print("")

    
