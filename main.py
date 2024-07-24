import tkinter as tk

class Mycalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("430x932")
        self.root.title("My calculator")

        self.label = tk.Label(self.root, text="Hello DIP02",font=("Arial", 18))
        self.label.pack()

        self.buttonAc = tk.Button(self.root, text="AC" , height=92, width=92)
        self.button.place(x=0, y=323)

        self.button7 = tk.Button(self.root, text="7" , height=92, width=92)
        self.button.place(x=0, y=428)

        self.button4 = tk.Button(self.root, text="4" , height=92, width=92)
        self.button.place(x=0, y=533)

        self.button1 = tk.Button(self.root, text="1" , height=92, width=92)
        self.button.place(x=0, y=638)

        self.button0 = tk.Button(self.root, text="0" , height=92, width=92)
        self.button.place(x=0, y=638)


        self.root.mainloop()

Mycalculator()