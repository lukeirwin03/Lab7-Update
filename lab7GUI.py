from curses import window
from tkinter import *
from tkinter import ttk
from lab7Main import *

class GUI:

    def __init__(self, window):
        self.window = window

        self.whichFunc = IntVar()

        organize = Frame(window, width=300, highlightbackground='blue', highlightthickness=2)
        organize.grid(padx=2,pady=2)

        self.mainLabel = Label(organize, text='Pick a Function: ')
        self.mainLabel.grid(row=1, column=0)


        self.whichFunc = IntVar()
 
        self.pickFuncOne = Radiobutton(organize, text = 'One', variable=self.whichFunc, value = 1)
        self.pickFuncOne.grid(row=1,column=1)
        self.pickFuncTwo = Radiobutton(organize, text = 'Two',variable=self.whichFunc, value = 2)
        self.pickFuncTwo.grid(row=1,column=2)
        self.pickFuncThree = Radiobutton(organize, text = 'Three',variable=self.whichFunc, value = 3)
        self.pickFuncThree.grid(row=1,column=3)

        goButton = Button(organize, text='Go',width=4, command=self.click)
        goButton.grid(row=2, column=1, columnspan=2)



    def click(self):
        self.pick = self.whichFunc.get()
        if(self.pick == 1):
            funcOne = Toplevel()
            funcOne.title('Func One')
            funcOne.geometry('240x70')
            outline = Frame(funcOne, highlightbackground='red', highlightthickness=2)
            outline.grid(rowspan=5, columnspan=5, padx=3, pady=3)
            self.funcLabel = Label(outline, text='Enter an Int: ')
            self.funcLabel.grid(row=0, column=0, columnspan=2)
            self.funcEntry = Entry(outline, width=6)
            self.funcEntry.grid(row=0, column=2, columnspan=3)
            self.funcExecButton = Button(outline, text='Go', width=2, command=self.execFunc)
            self.funcExecButton.grid(row=0,column=5, padx=2)
            self.outLabel = Label(outline)
            self.outLabel.grid(row=3, column=3, columnspan=5)
            


    def execFunc(self):
        num = int(self.funcEntry.get())
        self.funcEntry.delete(0,END)
        if(self.pick == 1):
            self.outLabel.config(text = f'{one(num)}')



        



