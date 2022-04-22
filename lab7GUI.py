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
            self.createFuncOneWin()
            
        if(self.pick == 2):
            self.createFuncTwoWin()

        if(self.pick == 3):
            self.createFuncThreeWin()

    def createFuncOneWin(self):
        funcOne = Toplevel()
        funcOne.title('Func One')
        funcOne.geometry('240x70')
        outline = Frame(funcOne, highlightbackground='red', highlightthickness=2)
        outline.grid(rowspan=5, columnspan=5, padx=3, pady=3)
        self.funcLabel = Label(outline, text='Enter an Int: ')
        self.funcLabel.grid(row=0, column=0, columnspan=2)
        self.funcEntry1 = Entry(outline, width=6)
        self.funcEntry1.grid(row=0, column=2, columnspan=3)
        self.funcExecButton = Button(outline, text='Go', width=2, command=self.execFunc)
        self.funcExecButton.grid(row=0,column=5, padx=2)
        self.outLabel = Label(outline)
        self.outLabel.grid(row=3, column=3, columnspan=10)

    def createFuncTwoWin(self):
        funcTwo = Toplevel()
        funcTwo.title('Func Two')
        funcTwo.geometry('260x100')
        outline = Frame(funcTwo, highlightbackground='red', highlightthickness=2)
        outline.grid(rowspan=5, columnspan=5, padx=3, pady=3)
        self.funcLabel1 = Label(outline, text='Enter Int for Base: ')
        self.funcLabel1.grid(row=0, column=0, columnspan=2)
        self.funcLabel1 = Label(outline, text='Enter Int for Power: ')
        self.funcLabel1.grid(row=1, column=0, columnspan=2)
        self.funcEntry1 = Entry(outline, width=6)
        self.funcEntry1.grid(row=0, column=2, columnspan=3)
        self.funcEntry2 = Entry(outline, width=6)
        self.funcEntry2.grid(row=1, column=2, columnspan=3)
        self.funcExecButton = Button(outline, text='Go', width=2, command=self.execFunc)
        self.funcExecButton.grid(row=0,column=5, padx=2)
        self.outLabel = Label(outline)
        self.outLabel.grid(row=3, column=3, columnspan=5)

    def createFuncThreeWin(self):
        funcOne = Toplevel()
        funcOne.title('Func Three')
        funcOne.geometry('240x70')
        outline = Frame(funcOne, highlightbackground='red', highlightthickness=2)
        outline.grid(rowspan=5, columnspan=5, padx=3, pady=3)
        self.funcLabel = Label(outline, text='Enter an Int: ')
        self.funcLabel.grid(row=0, column=0, columnspan=2)
        self.funcEntry1 = Entry(outline, width=6)
        self.funcEntry1.grid(row=0, column=2, columnspan=3)
        self.funcExecButton = Button(outline, text='Go', width=2, command=self.execFunc)
        self.funcExecButton.grid(row=0,column=5, padx=2)
        self.outLabel = Label(outline)
        self.outLabel.grid(row=3, column=3, columnspan=5)

    def execFunc(self):
        '''
        TODO: Implement the check method to account for the user inputting a non-int type
        '''
        if(self.pick == 1):
            check(self.funcEntry1.get())
            num = int(self.funcEntry1.get())
            self.funcEntry1.delete(0,END)
            self.outLabel.config(text = f'{one(num)}')
        if(self.pick == 2):
            check(self.funcEntry1.get(),self.funcEntry2.get())
            num1 = int(self.funcEntry1.get())
            num2 = int(self.funcEntry2.get())
            self.funcEntry1.delete(0, END)
            self.funcEntry2.delete(0, END)
            self.outLabel.config(text = f'{two(num1, num2)}')
        if(self.pick == 3):
            check(self.funcEntry1.get())
            num = int(self.funcEntry1.get())
            self.funcEntry1.delete(0, END)
            self.outLabel.config(text = f'{three(num)}')
