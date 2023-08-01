from tkinter import *


def submit():
    username = entry.get()
    print("Hello %s, please have a nice day :)" % username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get())-1, END)


def view():
    entry.config(show="")


window = Tk()

entry = Entry(window,
              font=("Arial", 30, 'bold'),
              bg="black",
              fg="green",
              show="*")

entry.pack(side=LEFT)

s_button = Button(window,
                  text="Submit",
                  command=submit)
d_button = Button(window,
                  text="Delete",
                  command=delete)
back_button = Button(window,
                     text="Backspace",
                     command=backspace)
v_button = Button(window,
                  text="view",
                  command=view)

s_button.pack(side=RIGHT)
d_button.pack(side=RIGHT)
back_button.pack(side=RIGHT)
v_button.pack(side=RIGHT)

window.mainloop()
