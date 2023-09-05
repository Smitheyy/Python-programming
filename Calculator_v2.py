from tkinter import *

def button_press(num):
  global equation_text

  equation_text += str(num)

  equation_label.set(equation_text)


def equals():
  
  global equation_text

  try:
       
    total = str(eval(equation_text))

    equation_label.set(total)

    equation_text = total

  except ZeroDivisionError:
   equation_label.set('Arithmetic error!')

   equation_text = ""

  except SyntaxError:
    equation_label.set('Syntax error!')

    equation_text = ""

def clear():
  global equation_text

  equation_label.set("")

  equation_text = ""


root = Tk()

root.title("Calculator")
root.geometry('500x500')

equation_text = ""

equation_label = StringVar()

label = Label(root, textvariable=equation_label, font=('Arial', 20), bg='black', width=24, height=2, fg='green')
label.pack()

frame = Frame(root)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: button_press(1), bg='black', fg='green')
button1.grid(row=3, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: button_press(2), bg='black', fg='green')
button2.grid(row=3, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: button_press(3), bg='black', fg='green')
button3.grid(row=3, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: button_press(4), bg='black', fg='green')
button4.grid(row=2, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: button_press(5), bg='black', fg='green')
button5.grid(row=2, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: button_press(6), bg='black', fg='green')
button6.grid(row=2, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: button_press(7), bg='black', fg='green')
button7.grid(row=1, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: button_press(8), bg='black', fg='green')
button8.grid(row=1, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: button_press(9), bg='black', fg='green')
button9.grid(row=1, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: button_press(0), bg='black', fg='green')
button0.grid(row=4, column=1)

plus = Button(frame, text='+', height=4, width=9, font=35, command=lambda: button_press('+'), bg='black', fg='green')
plus.grid(row=3, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35, command=lambda: button_press('-'), bg='black', fg='green')
minus.grid(row=2, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35, command=lambda: button_press('*'), bg='black', fg='green')
multiply.grid(row=1, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35, command=lambda: button_press('/'), bg='black', fg='green')
divide.grid(row=0, column=3)

decimal = Button(frame, text='.', height=4, width=9, font=35, command=lambda: button_press('.'), bg='black', fg='green')
decimal.grid(row=4, column=2)

equal = Button(frame, text='=', height=4, width=9, font=35, command=equals, bg='black', fg='green')
equal.grid(row=4, column=3)

clear = Button(frame, text='<---', height=4, width=9, font=35, command=clear, bg='black', fg='green')
clear.grid(row=0, column=2)

root.mainloop()
