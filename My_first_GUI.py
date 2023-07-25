from tkinter import *

count = 0


def click():
    global count
    print("BOINK")
    count += 1
    print("+", count, " MY LAD!")


# widgets = GUI elements: buttons, textboxes, labels
# windows = container to holding or containing widgets


gandalf = Tk()  # instantiate an instance of window
gandalf.geometry("420x420")
gandalf.title("Kacper's great window")

saruman = Tk()
saruman.geometry("200x200")
saruman.title("Kacper's second smaller window")

saruman.config(background="black")
gandalf.config(background="black")

# icon = PhotoImage(file='')
# gandalf.iconphoto(True, icon)   # it should change the displayed icon in the upper left corner, but it doesn't....
# I can use a hex color picker also

label_s = Label(saruman,
                text='Wanted!',
                font=('Arial', 40, 'bold'),
                background="black", fg='red',
                relief=RAISED,
                bd=0,
                padx=750,
                pady=350,
                )  # there is also image= and compound= they are related to the image that u would like to add

# label.pack()
label_s.place(x=100, y=100)
image = PhotoImage(file='emoji.png')

button = Button(gandalf,
                text='Click me ;)',
                command=click,
                font=('Comic Sans', 30),
                fg="#00FF00",
                bg='black',
                activeforeground="#00FF00",
                activebackground='black',
                state=ACTIVE,
                image=image,
                compound=TOP)
button.pack()

gandalf.mainloop()  # it displays the window, listen for events
