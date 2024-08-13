import tkinter as tk

class Mycalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("390x844")
        self.root.title("My calculator")

        self.label = tk.Label(self.root, text="DIP Calculator",font=("Arial", 18))
        self.label.pack()

        self.buttonC = tk.Button(self.root, text="c", height=5 , width=8)
        self.buttonC.place(x=19, y=347)

        self.buttonB = tk.Button(self.root, text="()", height=5 , width=8)
        self.buttonB.place(x=112, y=347)

        self.buttonP = tk.Button(self.root, text="%", height=5 , width=8)
        self.buttonP.place(x=205, y=347)

        self.buttonD = tk.Button(self.root, text="÷", height=5 , width=8)
        self.buttonD.place(x=298, y=347)

        self.button7 = tk.Button(self.root, text="7", height=5 , width=8)
        self.button7.place(x=19, y=442)

        self.button8 = tk.Button(self.root, text="8", height=5 , width=8)
        self.button8.place(x=112, y=442)

        self.button9 = tk.Button(self.root, text="9", height=5 , width=8)
        self.button9.place(x=205, y=442)

        self.buttonmultiply = tk.Button(self.root, text="x", height=5 , width=8)
        self.buttonmultiply.place(x=298, y=442)

        self.button4 = tk.Button(self.root, text="4", height=5 , width=8)
        self.button4.place(x=19, y=537)

        self.button5 = tk.Button(self.root, text="5", height=5 , width=8)
        self.button5.place(x=112, y=537)

        self.button6 = tk.Button(self.root, text="6", height=5 , width=8)
        self.button6.place(x=205, y=537)

        self.buttonminus = tk.Button(self.root, text="-", height=5 , width=8)
        self.buttonminus.place(x=298, y=537)

        self.button1 = tk.Button(self.root, text="1", height=5 , width=8)
        self.button1.place(x=19, y=632)

        self.button2 = tk.Button(self.root, text="2", height=5 , width=8)
        self.button2.place(x=112, y=632)

        self.button3 = tk.Button(self.root, text="3", height=5 , width=8)
        self.button3.place(x=205, y=632)

        self.buttonplus = tk.Button(self.root, text="+", height=5 , width=8)
        self.buttonplus.place(x=298, y=632)

        self.buttonoverspend = tk.Button(self.root, text="+/-", height=5 , width=8)
        self.buttonoverspend.place(x=19, y=727)

        self.button0 = tk.Button(self.root, text="0", height=5 , width=8)
        self.button0.place(x=112, y=727)

        self.buttondecimal = tk.Button(self.root, text=".", height=5 , width=8)
        self.buttondecimal.place(x=205, y=727)

        self.buttonequal = tk.Button(self.root, text="=", height=5 , width=8)
        self.buttonequal.place(x=298, y=727)

        self.root.mainloop()

Mycalculator()