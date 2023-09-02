from tkinter import *
from tkinter import filedialog


def openFile():
  file_path = filedialog.askopenfilename(
                             title="File opener",
                             filetypes=(
                               ("TXT files", ".txt"),
                               ("Python files", ".py"),
                               ("HTML files", ".html"),
                               ("All files", ".*")
                             ))
    
  if file_path is None:
    return
  
  file = open(file_path, 'r')
  print(file.read())
  file.close


def saveFile():
  file = filedialog.asksaveasfile(
                           title="File saver",
                           defaultextension='.txt',
                           filetypes=(
                               ("TXT files", ".txt"),
                               ("Python files", ".py"),
                               ("HTML files", ".html"),
                               ("All files", ".*")
                           ))
  
  if file is None:
    return
  
  storage_t = str(text.get(1.0, END))
  file.write(storage_t )
  file.close


def cutS(event):
  global selected
  
  try:
    if event:
      selected = window.clipboard_get()
    
    else:  
      if text.selection_get():
        selected = text.selection_get() # grab selected text from text box
        text.delete(1.0, END) # deletes whatever it is that needs cutting
        window.clipboard_clear()
        window.clipboard_append(selected)
  
  except TclError as k:
    print("Please select the text before moving on!")
    print(k)
    print('---------------------------------------------------------')


def copyS(event):
  global selected
  
  try:
    if event:
      selected = window.clipboard_get()
    
    else:  
      if text.selection_get():
        selected = text.selection_get()
        window.clipboard_clear()
        window.clipboard_append(selected)
  
  except TclError as k:
    print("Please select the text before moving on!")
    print(k)
    print('---------------------------------------------------------')

  

def pasteS(event):
  global selected
    
  if event:
    selected = window.clipboard_get()
  
  else:      
    if selected:
      position = text.index(INSERT)
      text.insert(position, selected)


window = Tk()

window.bind('<Control-Key-x>', cutS)
window.bind('<Control-Key-c>', copyS)
window.bind('<Control-Key-x>', pasteS)

global selected
selected = False

openImage = PhotoImage(file="open.png",
                       )
saveImage = PhotoImage(file="save.png",
                       )
exitImage = PhotoImage(file="stop.png",
                       )
cutImage = PhotoImage(file='cut.png'
                      )
copyImage = PhotoImage(file='copy.png'
                      )
pasteImage = PhotoImage(file='paste.png'
                      )

menubar = Menu(window,)

window.config(menu=menubar)

fileMenu = Menu(menubar,
                tearoff=0,
                font=('My Boli', 15))
menubar.add_cascade(label="File",                    
                    menu=fileMenu,)
                

fileMenu.add_command(label="Open", 
                     command=openFile,
                     foreground="purple",
                     image=openImage,
                     compound=LEFT)
fileMenu.add_command(label="Save", 
                     command=saveFile,
                     foreground="purple",
                     image=saveImage,
                     compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",
                     command=quit,
                     foreground="purple",
                     image=exitImage,
                     compound=LEFT)


edit_Menu = Menu(menubar,
                 tearoff=0,
                 font=('My Boli', 15))
menubar.add_cascade(label='Edit',
                    menu=edit_Menu)

Cut = edit_Menu.add_command(label='Cut       (Ctrl+x)',
                      command=lambda: cutS(False),
                      foreground='purple',
                      image=cutImage,
                      compound=LEFT)
Copy = edit_Menu.add_command(label='Copy       (Ctrl+c)',
                      command=lambda: copyS(False),
                      foreground='purple',
                      image=copyImage,
                      compound=LEFT)
Paste = edit_Menu.add_command(label='Paste       (Ctrl+v)',
                      command=lambda: pasteS(False),
                      foreground='purple',
                      image=pasteImage,
                      compound=LEFT)

text = Text(window,
            bg="light yellow",
            fg="purple",
            height=10,
            width=20,
            padx=20,
            pady=20,
            )
text.pack()

window.mainloop()
