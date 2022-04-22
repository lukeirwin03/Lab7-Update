from tkinter import *
from lab7GUI import *
from LukeIrwin7_1 import *

def main():
    window = Tk()
    window.title('Lab 7')
    window.geometry('295x70')
    window.resizable(False,False)
    
    widgets = GUI(window)

    window.mainloop()




if __name__ == '__main__':
    main()