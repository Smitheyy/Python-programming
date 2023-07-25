from tkinter import *

count = 0


def click():
    global count
    print("You clicked the button....")
    count += 1
    print(count)
# widgets = GUI elements: buttons, textboxes, labels
# windows = container to holding or containing widgets


gandalf = Tk()  # instantiate an instance of window
gandalf.geometry("420x420")
gandalf.title("Kacper's great window")

# icon = PhotoImage(file='')
# gandalf.iconphoto(True, icon)   # it should change the displayed icon in the upper left corner, but it doesn't....
gandalf.config(background="white")   # I can use a hex color picker also

label = Label(gandalf,
              text='Wanted!',
              font=('Arial', 40, 'bold'),
              background="white", fg='red',
              relief=RAISED,
              bd=10,
              padx=30,
              pady=30,
              )     # there is also image= and compound= they are related to the image that u would like to add

# label.pack()
label.place(x=100, y=100)
image = PhotoImage(file='emoji.png')

button = Button(gandalf,
                text='Click me :)',
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
