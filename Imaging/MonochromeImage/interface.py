#import tkinter.ttk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import img_gen

fname = ""
outputFile = ""

def openFile():
    file = filedialog.askopenfile(mode="r", title="Choose an input file")
    if file != None:
        newFilename = ""

        r = False
        override = False
        
        for char in str(file):
            if char == "'" and r == False:
                r = True

            elif char != "'" and r == True and override == False:
                newFilename += char

            elif char == "'" and r == True:
                r = False
                override = True

        global fname
        fname = newFilename
        print(f"Filename (Tkinter): {fname}")
        
      
    else:
        pass

def setOutput():
    file = filedialog.asksaveasfile(title="Choose an output file")
    if file != None:
        newFilename = ""

        r = False
        override = False
        
        for char in str(file):
            if char == "'" and r == False:
                r = True

            elif char != "'" and r == True and override == False:
                newFilename += char

            elif char == "'" and r == True:
                r = False
                override = True

        global outputFile
        outputFile = newFilename
        print(f"Output File (Tkinter): {outputFile}")
        
      
    else:
        pass


window = Tk()
window.title("Monochromatic Image Converter (Python)")
window.config(background="#FFF")
window.geometry("640x480")
window.anchor("center")

tx1 = Label (window, text="Monochromatic Image Converter", bg="#FFF", fg="#000", font="none 12 normal")
tx1.pack(side="top", pady="25")

tx3 = Label (window, text="Input file:", bg="#FFF", fg="#000", font="none 12 normal", pady=0)
tx3.pack(side="top", pady="25")


openBtn = Button(text="Browse...", width="20", pady="2", command=lambda: openFile())
openBtn.pack(side="top", pady="10")




tx4 = Label (window, text="Output file:", bg="#FFF", fg="#000", font="none 12 normal", pady=0)
tx4.pack(side="top", pady="25")

outputBtn = Button(text="Set...", width="20", pady="2", command=lambda: setOutput())
outputBtn.pack(side="top", pady="10")




sendBtn = Button(text="Convert", width="20", pady="2", command=lambda: img_gen.run(fname, outputFile, i.get()))
sendBtn.pack(side="top", pady="10")

i = IntVar()
c = Checkbutton(text="Invert", variable=i, bg="#FFF")
c.pack(side="top")

window.mainloop()
