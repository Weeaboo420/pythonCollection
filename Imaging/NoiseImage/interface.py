import tkinter.ttk
from tkinter import *

import img_gen

window = Tk()
window.title("S.N.I.G.")
window.config(background="#FFF")
window.geometry("640x480")
window.anchor("center")

tx1 = Label (window, text="Shaded Noisy Image Generator", bg="#FFF", fg="#000", font="none 12 normal")
tx1.pack(side="top", pady="25")

#ph1 = PhotoImage(file="girls.gif")
#Label2 = Label(image=ph1)
#Label2.image = ph1
#Label2.pack()

tx2 = Label (window, text="Resolution:", bg="#FFF", fg="#000", font="none 12 bold")
tx2.pack(side="top", pady="25")
tx5 = Label (window, text="Format: WIDTHxHEIGHT", bg="#FFF", fg="#000", font="none 12 normal", pady=0)
tx5.pack(side="top", pady="5")


res_in = ttk.Entry()
res_in.pack(side="top")

tx3 = Label (window, text="RGB Values:", bg="#FFF", fg="#000", font="none 12 bold", pady=0)
tx3.pack(side="top", pady="25")
tx4 = Label (window, text="Format: (x, x, x)", bg="#FFF", fg="#000", font="none 12 normal", pady=0)
tx4.pack(side="top", pady="5")

rgb_in = ttk.Entry()
rgb_in.pack(side="top")


#sentVars = img_gen.run(100, 100, "(0, 50, 255)")

sendBtn = Button(text="Send", width="20", pady="2", command=lambda: (img_gen.run(res_in.get(), rgb_in.get())))
sendBtn.pack(side="top", pady="10")

window.mainloop()
