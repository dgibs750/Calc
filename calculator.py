# Python program to create a GUI calculator

from tkinter import *


# Creates a calculator class
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Calculator")

        # create screen widget
        self.screen = Text(master, state = 'disabled', width = 30, height = 2,
            background = "grey", foreground = "black", font = ('Helvetica', 30, 'bold'))
        
        # position of screen
        self.screen.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)
        self.screen.configure(state = 'normal')

        # initialize screen value as empty
        self.equation = ''

        # create buttons
        b1 = self.createButton(7)
        b2 = self.createButton(8)
        b3 = self.createButton(9)
        b4 = self.createButton(u"\u232B", None)
        b5 = self.createButton(4)
        b6 = self.createButton(5)
        b7 = self.createButton(6)
        b8 = self.createButton(u"\u00F7")
        b9 = self.createButton(1)
        b10 = self.createButton(2)
        b11 = self.createButton(3)
        b12 = self.createButton('*')
        b13 = self.createButton('.')
        b14 = self.createButton(0)
        b15 = self.createButton('+')
        b16 = self.createButton('-')
        b17 = self.createButton('=', None, 34)

        # store buttons in a list
        buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17]

        count = 0

        # place buttons in grid
        for row in range(1, 5):
            for column in range(4):
                buttons[count].grid(row = row, column = column, padx = 0, pady = 5)
                count += 1
        # place '=' button
        buttons[16].grid(row = 5, column = 0, columnspan = 4)

    def createButton(self, val, write = True, width = 10, height = 3):
        return Button(self.master, text = val, command = lambda: self.click(val, write), 
            width = width, height = height, bd = 4, font = ('Helvetica', 16, 'bold'))

    def click(self, text, write):
        # handles what happes when button is clicked
        if write == None:
            if text == '=' and self.equation:
                self.equation = re.sub(u"\u00F7", '/', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer, newline = True)
            elif text == u"\u232B":
                self.clear_screen()


        else:
            self.insert_screen(text)


    def clear_screen(self):
        # clears screen
        self.equation = ''
        self.screen.configure(state = 'normal')
        self.screen.delete('1.0', END)


    def insert_screen(self, value, newline = False):
        self.screen.configure(state = 'normal')
        self.screen.insert(END, value)
        # record every value inserted
        self.equation += str(value)
        self.screen.configure(state = 'disabled')




root = Tk()
my_gui = Calculator(root)
root.mainloop()