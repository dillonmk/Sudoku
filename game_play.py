from tkinter import*
from tkinter import ttk
import numpy as np


#Test Board
board = np.array([[1,1,1,4,4,4,7,7,7],[1,1,1,4,4,4,7,7,7],[1,1,1,4,4,4,7,7,7],
                [2,2,2,5,5,5,8,8,8],[2,2,2,5,5,5,8,8,8],[2,2,2,5,5,5,8,8,8],
                [3,3,3,6,6,6,9,9,9],[3,3,3,6,6,6,9,9,9],[3,3,3,6,6,6,9,9,9]])

value_selected = int(1)

class board_button:
    'When we create instances in a class, they recieve the instance...'
    '...as the first argument. Self is used by convention'
    'initial_state: True = non empty original square'
    'initial_state: False = empty square for player to select'
    def __init__(self, row, column, value, initial_state,board,frame_selct):
        self.row = row
        self.column = column
        ttk.Button(frame_selct, text = str(value)).grid(column=self.column, row = self.row, sticky = 'NSEW')


    'Each function in a class automatically takes the instance as first arg'
    'intended_value will be the value the player wants to place in square'
    def place_select(self,intended_value):
        if self.initial_state == True:
            pass
        else:
            self.value = intended_value

    def place_value(self,board):
        if self.initial_state == False:
            board[self.row,self.column] = value_selected
        else:
            print('Invalid Selection')

class side_buttons:

    def __init__(self, row, column, text, root):
        self.row = row
        self.column = column
        self.text = text
        ttk.Button(root, text = self.text).grid(column = self.column, row = self.row, sticky = N)


#Setting Up the main Frame
root = Tk()
root.title("App Bar Title")

'Configuring only sets the size of each induvidual row or column...'
'...does not specify how many rows or columns'
root.columnconfigure(0, weight = 9)
root.rowconfigure(1, weight = 9)



top_frame = ttk.Frame(root).grid(column = 0, row = 0)
side_frame = ttk.Frame(root).grid(column = 1, row = 0, rowspan = 2)
board_frame = ttk.Frame(root).grid(column = 0, row=1, sticky=(N, W, E, S))
'''
board_frame.columnconfigure(tuple(range(9)), weight=1)
board_frame.rowconfigure(tuple(range(9)), weight=1)
'''

#Title
ttk.Label(board_frame, text = "").grid(column = 5,row=0,sticky=N)
#Timer
ttk.Label(board_frame, text = "Time:").grid(column = 0, row = 0, sticky = N)




# Using a loop to fill a list of buttons
def create_buttons(board):
    list_buttons = []
    for row in range(9):
        for column in range(9):
            if board[row,column]==0:
                list_buttons.append(board_button(row+3, column, '', False, board, board_frame))
            elif board[row,column] != 0:
                list_buttons.append(board_button(row+3, column, board[row,column], True, board, board_frame))


    '''
    def main():
    Players = 0
    list_of_players = []
    for i in range(5):
        list_of_players.append(Player("Joe", 5, "Machine gun", 22, i+1))
        print list_of_players[i]
    '''

create_buttons(board)
'''
select_1 = ttk.Button(root, text ="1").grid(column = 0, row = 2)
select_2 = ttk.Button(root, text ="2").grid(column = 1, row = 2)
select_3 = ttk.Button(root, text ="3").grid(column = 2, row = 2)
select_4 = ttk.Button(root, text ="4").grid(column = 3, row = 2)
select_5 = ttk.Button(root, text ="5").grid(column = 4, row = 2)
select_6 = ttk.Button(root, text ="6").grid(column = 5, row = 2)
select_7 = ttk.Button(root, text ="7").grid(column = 6, row = 2)
select_8 = ttk.Button(root, text ="8").grid(column = 7, row = 2)
select_9 = ttk.Button(root, text ="9").grid(column = 8, row = 2)


pause_button = side_buttons(0,10,"Pause",root)
erase_button = side_buttons(2,10,"Erase",root)
undo_button = side_buttons(4,10,"Undo",root)
complete_button = side_buttons(6,10,"Complete",root)
give_up_button = side_buttons(8,10,"Quit",root)

easy_difficulty = ttk.Button(root, text = "Easy").grid(column = 3, row = 12, sticky = "NSEW")
medium_difficulty = ttk.Button(root, text = "Medium").grid(column = 5,row = 12,sticky = "NSEW")
hard_difficulty = ttk.Button(root,text = "Hard").grid(column = 7,row = 12,sticky = "NSEWE")
'''

root.mainloop()
