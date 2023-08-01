from tkinter import *


def submit():
    print("The temperature is " + str(scale.get()) + " degrees celsius")


window = Tk()

window.config(bg="white")


icon = PhotoImage(file="weighing_scales.png")
window.iconphoto(True, icon)

flame_image = PhotoImage(file="flame.png")

flame_label = Label(image=flame_image)

flame_label.pack()

snowflake_image = PhotoImage(file="Snowflake.png")
snowflake_label = Label(image=snowflake_image,
                        compound=TOP)

snowflake_label.pack(side=BOTTOM)

scale = Scale(window,
              from_=100,
              to=0,
              length=700,
              width=30,
              orient=VERTICAL,  # or horizontal
              font=("Arial", 20, "bold"),
              tickinterval=10,  # this adds numeric indicators for values
              showvalue=False,  # hide current value
              resolution=5,     # increment of slider
              troughcolor="#69EAFF",
              fg="#FF1C00",
              bg="black",
              )

# scale.set(100)  # it sets where the scale should stop at
scale.set(((scale['from']-scale['to']) / 2) + scale['to'])    # makes the scale stand at the middle of its values

button = Button(window,
                text="SUBMIT",
                command=submit,
                fg="#FF1C00",
                bg="black",
                )

scale.pack()
button.place(x=865, y=805)
window.mainloop()
