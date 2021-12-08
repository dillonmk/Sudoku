from tkinter import*
from tkinter import ttk



class board_button:

    'When we create instances in a class, they recieve the instance...'
    '...as the first argument. Self is used by convention'
    'initial_state: True = non empty original square'
    'initial_state: False = empty square for player to select'
    def __init__(self, row, column, value, initial_state,root):
        self.row = row
        self.column = column
        self.value = value
        self.initial_state = initial_state
        ttk.Button(root, text = "Value").grid(column=self.column, row = self.row, sticky = N)








    'Each function in a class automatically takes the instance as first arg'
    'intended_value will be the value the player wants to place in square'
    def place_select(self,intended_value):
        if self.initial_state == True:
            pass
        else:
            self.value = intended_value


class side_buttons:

    def __init__(self, row, column, text):
        self.row = row
        self.column = column
        self.text = text

root = Tk()
root.mainloop()
root.title("Sudoku")
button_1 = board_button(0,0,4,True,root)
