from tkinter import *


class window():

    def __init__(self, title, x, y, bg, anchor):

        self.title = title
        self.x = x
        self.y = y

        self.bg = bg
        self.anchor = anchor
        p = Tk()

        if len(title) > 0:
            p.title(title)

        if x > 50 and y > 50:
            p.geometry(f"{x}x{y}")

        if len(bg) >= 3 and len(bg) < 8:
            try:
                p.config(background=bg)
            except:
                raise ValueError("Invalid bg-color")

        p.mainloop()

#window = Tk()
#window.title("Yuri")
#window.config(background="#333")
#window.geometry("640x480")
#window.anchor("center")

#tx1 = Label (window, text="Yuri Love", bg="#333", fg="#FFF", font="none 12 bold")
#tx1.pack()

#ph1 = PhotoImage(file="girls.gif")
#Label2 = Label(image=ph1)
#Label2.image = ph1
#Label2.pack()

#window.mainloop()
