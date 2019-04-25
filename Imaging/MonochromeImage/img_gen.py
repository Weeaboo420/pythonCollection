from PIL import Image
from PIL import ImageDraw

import os, random as ran, time


def generate(n, size_x, size_y, out, invert):

    myImage = Image.new("RGB", (size_x, size_y), 0)
    resX, resY = myImage.size
    original = Image.open(n)
    d = ImageDraw.Draw(myImage)
    t1 = time.process_time()

    for y in range(resY):
        for x in range(resX):

            rgb = original.getpixel((x, y))

            lum = []
            for val in rgb:
                if len(lum) < 3:
                    lum.append(val)
                else:
                    pass
            #print(lum)
            #b = max(lum)
            r = round(0.2126*lum[0])
            g = round(0.7152*lum[1])
            b = round(0.0722*lum[2])
            l = r+g+b

            if invert == 1:
                l = 255 - l
            else:
                pass
            
            #myImage.putpixel((x, y), (l,l,l)) this is SLOW
            d.point((x, y), (l,l,l))

    
    try:    
        myImage.save(out)
        t2 = time.process_time()
        t3 = round(t2-t1, 3)
        print(f"Saved image ({resX}x{resY}) in {t3}s")
      
    except:
        print("ERROR: Could not save file")

#while True:
def run(inputName, outputName, invert):
    if len(inputName) > 0 and len(outputName) > 0:
        print(f"(IMG_GEN) Filename: {inputName}")
        print(f"Invert: {invert}")
        
        temp = Image.open(inputName)
        name, width, height = temp.filename, temp.width, temp.height
        temp.close()
        #print(name, width, height)
        generate(name, width, height, outputName, invert)

    else:
        print("ERROR: Filename must be longer than 0 characters!")


