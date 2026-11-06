from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Denomination Counter")
root.geometry("650x400")
root.config(bg="light blue")

Label(root, text = "Welcome to the Denomination Counter!", font=("Arial", 16), bg="light blue").place(x=150, y=120)

Label(root, text= "Calculate the number of notes in your amount.", bg="light blue").place(x=175, y=170)

def topwin():
    top = Toplevel(root)
    top.title("Denomination Calculator")
    top.geometry("500x350")
    top.config(bg="light grey")

    Label(top, text="Enter Total Amount", bg="light grey").place(x=180, y=30)

    entry = Entry(top)
    entry.place(x=170, y=60)

    Label(top, text = "Number of Notes", bg="light grey").place(x=190, y=120)

    Label(top, text="2000", bg = "light grey").place(x=150, y=160)

    Label(top, text="500", bg = "light grey").place(x=150, y=200)

    Label(top, text="100", bg = "light grey").place(x=150, y=240)

    t1 = Entry(top)
    t1.place(x=230, y=160)

    t2 = Entry(top)
    t2.place(x=230, y=200)

    t3 = Entry(top)
    t3.place(x=230, y=240)

    def calculator():
        try:
            amount = int(entry.get())

            n1 = amount // 2000
            amount = amount % 2000

            n2 = amount // 500
            amount = amount % 500

            n3 = amount // 100
            amount = amount % 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(0, n1)
            t2.insert(0, n2)
            t3.insert(0, n3)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    Button(top, text="Calculate", command=calculator,
           bg="brown", fg="white").place(x=210, y=290)
Button(root, text="Let's Get Started!",
       command=topwin, bg="brown", fg="white").place(x=265, y=230)

root.mainloop()