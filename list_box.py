# listbox = a listing of selectable text items within its own container

from tkinter import *


def submit():
    food = []

    for i in list_box.curselection():
        food.insert(i, list_box.get(i))
    print("You have ordered: ")

    for i in food:
        print(i)

    delete()


def add():
    list_box.insert(list_box.size(), Entry_box.get())
    list_box.config(height=list_box.size())


def delete():
    Entry_box.delete(0, END)
    list_box.config(height=list_box.size())


def remove():
    for i in reversed(list_box.curselection()):
        list_box.delete(i)

    list_box.config(height=list_box.size())


window = Tk()
window.config(bg="#8b572a")


list_box = Listbox(window,
                   bg="#f7ffde",
                   font=("Constantia", 35),
                   fg="#000000",
                   width=15,
                   relief=RAISED,
                   bd=1,
                   selectmode=MULTIPLE)

list_box.pack()

list_box.config(height=list_box.size())

Entry_box = Entry(window)
Entry_box.pack()

remove_b = Button(window,
                  text="REMOVE",
                  command=remove,
                  fg="#000000",
                  bg="#f7ffde",
                  relief=RAISED,
                  bd=1,
                  )

remove_b.pack()


submit_b = Button(window,
                  text="SUBMIT",
                  command=submit,
                  fg="#000000",
                  bg="#f7ffde",
                  relief=RAISED,
                  bd=1,
                  )

submit_b.pack()


delete_b = Button(window,
                  text="DELETE",
                  command=delete,
                  fg="#000000",
                  bg="#f7ffde",
                  relief=RAISED,
                  bd=1,
                  )

delete_b.pack()


add_b = Button(window,
               text="ADD",
               command=add,
               fg="#000000",
               bg="#f7ffde",
               relief=RAISED,
               bd=1,
               )

add_b.pack()


window.mainloop()
