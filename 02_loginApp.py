from tkinter import *
root = Tk()
root.geometry("400x400")
Label(root, text="Full Name").place(x=20, y=20)
name = Entry(root)
name.place(x=120, y = 20)

Label(root, text="Email").place(x = 20, y = 60)
email = Entry(root)
email.place(x=120, y = 60)

Label(root, text="Password").place(x = 20, y = 100)
password = Entry(root, show="*")
password.place(x=120, y = 100)

def display():
    textbox.insert(END, "Hey " + name.get() + "\nAccount Created!")

textbox = Text(root, height = 5, width = 35)
textbox.place(x = 20, y = 180)

Button(root, text = "Create Account", command = display).place(x=120, y = 140)

root.mainloop()