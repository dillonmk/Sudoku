from tkinter import*
from tkinter import ttk
import main
import numpy as np


board = np.array([[1,1,1,4,4,4,7,7,7],[1,1,1,4,4,4,7,7,7],[1,1,1,4,4,4,7,7,7],
                [2,2,2,5,5,5,8,8,8],[2,2,2,5,5,5,8,8,8],[2,2,2,5,5,5,8,8,8],
                [3,3,3,6,6,6,9,9,9],[3,3,3,6,6,6,9,9,9],[3,3,3,6,6,6,9,9,9]])

class board_button:

    'When we create instances in a class, they recieve the instance...'
    '...as the first argument. Self is used by convention'
    'initial_state: True = non empty original square'
    'initial_state: False = empty square for player to select'
    def __init__(self, row, column, value, initial_state,root):
        self.row = row
        self.column = column
        ttk.Button(root, text = str(value)).grid(column=self.column, row = self.row, sticky = 'NSEW')



    'Each function in a class automatically takes the instance as first arg'
    'intended_value will be the value the player wants to place in square'
    def place_select(self,intended_value):
        if self.initial_state == True:
            pass
        else:
            self.value = intended_value


class side_buttons:

    def __init__(self, row, column, text, root):
        self.row = row
        self.column = column
        self.text = text
        ttk.Button(root, text = self.text).grid(column = self.column, row = self.row, sticky = N)


#Setting Up the main Frame
root = Tk()
root.title("Sudoku")
mainframe = ttk.Frame(root, padding = "12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.grid_propagate(False)


'''
import Tkinter as tk

master = tk.Tk()

frame = tk.Frame(master, width=40, height=40) #their units in pixels
button1 = tk.Button(frame, text="btn")


frame.grid_propagate(False) #disables resizing of frame
frame.columnconfigure(0, weight=1) #enables button to fill frame
frame.rowconfigure(0,weight=1) #any positive number would do the trick

frame.grid(row=0, column=1) #put frame where the button should be
button1.grid(sticky="wens") #makes the button expand

tk.mainloop()

'''











root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.columnconfigure(6, weight=1)
root.columnconfigure(7, weight=1)
root.columnconfigure(8, weight=1)
root.columnconfigure(9, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)
root.rowconfigure(8, weight=1)
root.rowconfigure(9, weight=1)
root.rowconfigure(10, weight=1)


ttk.Label(mainframe, text = "SUDOKU MASTER").grid(column = 5,row=0,sticky=N)
ttk.Label(mainframe, text = "Time:").grid(column = 0, row = 0, sticky = N)

button_1 = board_button(1,0,4,True,root)

# Using a loop to fill a list of buttons
def create_buttons(board):
    list_buttons = []
    for row in range(9):
        for column in range(9):
            if board[row,column]==0:
                list_buttons.append(board_button(row+1, column, '', False, root))
            elif board[row,column] != 0:
                list_buttons.append(board_button(row+1, column, board[row,column], True, root))
'''
def main():
Players = 0
list_of_players = []
for i in range(5):
    list_of_players.append(Player("Joe", 5, "Machine gun", 22, i+1))
    print list_of_players[i]
'''
create_buttons(board)

pause_button = side_buttons(0,10,"Pause",root)

root.mainloop()
