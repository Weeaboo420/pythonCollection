from PIL import Image
import PIL, os, random

def generate(w, h):
    print(f"Generating image with a size of ({w}x{h})")
    newImage = Image.new("RGB", (w, h))


    #generate start position
    start = random.randint(1, w-2)
    print(f"Start position: ({start}, 0)")

    #generate end position
    end = random.randint(1, w-2)
    print(f"End position: ({end}, {h-1})")

    newImage.putpixel((start, 0), (255, 255, 255))
    newImage.putpixel((end, h-1), (255, 255, 255))

    #save the image
    scaledImage = newImage.resize((w*100, h*100))

    if os.path.isfile("mAzE.png"):
        os.remove("mAzE.png")

    scaledImage.save("mAzE.png")

run = True
while run:
    width, height = input("Maze width: "), input("Maze height: ")

    if len(width) > 0 and len(height) > 0:
        if width.isdigit() and height.isdigit():
            generate(int(width), int(height))

        else:
            print("")

    else:
        print("")
