from tkinter import *


def do():
    if z.get() == 1:
        print("You have agreed on being significant to somebody, outta boy!")
    else:
        print("Remember that you are important, never forget that. There are so many people that care about you, just have to notice them")


window = Tk()

z = IntVar()

photo = PhotoImage(file="Important-Icon.png")

check_box = Checkbutton(window,
                        text="I do make a difference to someone",
                        variable=z,
                        onvalue=1,
                        offvalue=0,
                        command=do,
                        font=("Arial", 30, "bold"),
                        fg="#00FF00",
                        bg="black",
                        image=photo,
                        compound=RIGHT)

check_box.pack()

window.mainloop()
