from tkinter import*
from tkinter import ttk
import numpy as np

board = np.array([[1,1,1,0,0,0,7,7,7],[1,1,1,4,4,4,7,7,7],[1,1,1,4,4,4,7,7,7],
                [2,2,2,5,5,5,0,0,0],[2,2,2,5,5,5,8,8,8],[2,2,2,5,5,5,8,8,8],
                [3,3,3,6,6,6,9,9,9],[3,3,3,6,6,6,9,9,9],[3,3,3,6,6,6,9,9,9]])
loaded_value = int(1)
####### Creating the button functions #######

# Number Buttons to select value... Pressing the button will 'load' the value.

def load(number):
    loaded_value = number
    print(loaded_value)

def create_game_frame(container):
    #Creating the frame that will contain the board/grid

    frame = ttk.LabelFrame(container, text = 'Game Board')
    frame.columnconfigure(0,weight = 1)
    frame.columnconfigure(1,weight = 1)
    frame.columnconfigure(2,weight = 1)
    frame.columnconfigure(3,weight = 1)
    frame.columnconfigure(4,weight = 1)
    frame.columnconfigure(5,weight = 1)
    frame.columnconfigure(6,weight = 1)
    frame.columnconfigure(7,weight = 1)
    frame.columnconfigure(8,weight = 1)

    frame.rowconfigure(0,weight = 1)
    frame.rowconfigure(1,weight = 1)
    frame.rowconfigure(2,weight = 1)
    frame.rowconfigure(3,weight = 1)
    frame.rowconfigure(4,weight = 1)
    frame.rowconfigure(5,weight = 1)
    frame.rowconfigure(6,weight = 1)
    frame.rowconfigure(7,weight = 1)
    frame.rowconfigure(8,weight = 1)




    return(frame)

def create_number_frame(container):
    #This frame will contain the number buttons that will...
    #...be selected before clicking on the location that the user...
    #...wants to place that value
    frame = ttk.Frame(container)
    frame.columnconfigure(0,weight = 1)
    frame.columnconfigure(1,weight = 1)
    frame.columnconfigure(2,weight = 1)
    frame.columnconfigure(3,weight = 1)
    frame.columnconfigure(4,weight = 1)
    frame.columnconfigure(5,weight = 1)
    frame.columnconfigure(6,weight = 1)
    frame.columnconfigure(7,weight = 1)
    frame.columnconfigure(8,weight = 1)
    frame.rowconfigure(0, weight = 1)

    ttk.Button(frame, text = '1', command = lambda: load(1)).grid(column = 0, row = 0)
    ttk.Button(frame, text = '2', command = lambda: load(2)).grid(column = 1, row = 0)
    ttk.Button(frame, text = '3', command = lambda: load(3)).grid(column = 2, row = 0)
    ttk.Button(frame, text = '4', command = lambda: load(4)).grid(column = 3, row = 0)
    ttk.Button(frame, text = '5', command = lambda: load(5)).grid(column = 4, row = 0)
    ttk.Button(frame, text = '6', command = lambda: load(6)).grid(column = 5, row = 0)
    ttk.Button(frame, text = '7', command = lambda: load(7)).grid(column = 6, row = 0)
    ttk.Button(frame, text = '8', command = lambda: load(8)).grid(column = 7, row = 0)
    ttk.Button(frame, text = '9', command = lambda: load(9)).grid(column = 8, row = 0)

    #Padding around the buttons
    for widget in frame.winfo_children():
        widget.grid(padx = 3, pady = 3)

    return(frame)

def create_side_frame(container):
    #This frame will contain the buttons to ...
    #... pause, erase, undo, finish game, give up

    frame = ttk.LabelFrame(container, text = "Options")
    frame.columnconfigure(0, weight = 1)
    frame.rowconfigure(0, weight = 1)
    frame.rowconfigure(1, weight = 1)
    frame.rowconfigure(2, weight = 1)
    frame.rowconfigure(3, weight = 1)
    frame.rowconfigure(4, weight = 1)


    ttk.Button(frame, text = 'Pause').grid(column = 0, row = 0)
    ttk.Button(frame, text = 'Erase').grid(column = 0, row = 1)
    ttk.Button(frame, text = 'Undo').grid(column = 0, row = 2)
    ttk.Button(frame, text = 'Finish').grid(column = 0, row = 3)
    ttk.Button(frame, text = 'Give Up').grid(column = 0, row = 4)

    for widget in frame.winfo_children():
        widget.grid(padx = 3, pady = 3)

    return(frame)

def create_title_frame(container):
    #This frame will contain the title, timer, score?


    frame = ttk.Frame(container, style = 'frame.TFrame')


    frame.columnconfigure(0, weight = 1)
    frame.columnconfigure(1, weight = 1)
    frame.columnconfigure(2, weight = 1)
    frame.columnconfigure(3, weight = 1)
    frame.rowconfigure(0, weight = 1)

    time_label = ttk.Label(container, text = 'Time:')
    time_label.grid(column = 0, row = 0)

    timer = ttk.Label(container, text = '01:23')
    timer.grid(column = 1, row = 0)

    label = ttk.Label(container, text = "Sudoku")
    label.grid(column = 2, row = 0)


    for widget in frame.winfo_children():
        widget.grid(padx = 3, pady = 3)

    return(frame)

def create_difficulty_frame(container):
    #This frame will hold the buttons for stating a new game...
    #...based on difficulty selected
    frame = ttk.LabelFrame(container, text = "Difficulty")
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight = 1)
    frame.columnconfigure(1, weight = 1)
    frame.columnconfigure(2, weight = 1)

    ttk.Button(frame, text = "Easy").grid(column = 0, row = 0)
    ttk.Button(frame, text = "Medium").grid(column = 1, row = 0)
    ttk.Button(frame, text = "Hard").grid(column = 2, row = 0)

    for widget in frame.winfo_children():
        widget.grid(padx = 3, pady = 3)

    return(frame)


class board_button:

    def __init__(self, row, column, value, initial_state, board, frame_selct):
        self.row = row
        self.column = column
        ttk.Button(frame_selct, text = str(value)).grid(column=self.column, row = self.row, sticky = 'NSEW')

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

def create_buttons(board):
    list_buttons = []
    for row in range(9):
        for column in range(9):
            if board[row,column]==0:
                list_buttons.append(board_button(row+3, column, '', False, board, game_frame))
            elif board[row,column] != 0:
                list_buttons.append(board_button(row+3, column, board[row,column], True, board, game_frame))


def create_main_window():

    #root window
    root = Tk()
    root.title('Sudoku')


    root.columnconfigure(0, weight = 1)
    root.columnconfigure(1, weight = 1)
    root.rowconfigure(0, weight = 1)
    root.rowconfigure(1, weight = 1)
    root.rowconfigure(2, weight = 1)
    root.rowconfigure(3, weight = 1)

    title_frame = create_title_frame(root)
    title_frame.grid(column = 0, row = 0)

    number_frame = create_number_frame(root)
    number_frame.grid(column = 0, row = 1)

    global game_frame
    game_frame = create_game_frame(root)
    game_frame.grid(column = 0, row = 2)
    create_buttons(board)

    side_frame = create_side_frame(root)
    side_frame.grid(column = 1, row = 1, rowspan = 3)

    difficulty_frame = create_difficulty_frame(root)
    difficulty_frame.grid(column = 0, row = 3)

    root.mainloop()


create_main_window()
