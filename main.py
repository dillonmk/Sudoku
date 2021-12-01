#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 10:25:59 2021

@author: dillon
"""

"We are going to write some code to play sudoku" 

"First we are going to write a random sudoku game generator"

import random
import numpy as np



"""""""""Creating the Board"""""""""

"Columns"
n = int(9)
"Rows"
m = int(9)

"Empty 9x9 for the playing board"
board = np.zeros((n,m),dtype=int)

"This is going to be a matrix that tracks available numbers for each 'box'"
b = np.arange(1,10,1)
available_box = np.zeros((9,9),dtype = int)
for x in range(9):
    available_box[x] = b
  


## Box names will go down column then next column down etc.
## Box1  Box4  Box7
## Box2  Box5  Box8
## Box3  Box6  Box9


# Test Board
#board = np.array([[1,1,1,4,4,4,7,7,7],[1,1,1,4,4,4,7,7,7],[1,1,1,4,4,4,7,7,7],
#                [2,2,2,5,5,5,8,8,8],[2,2,2,5,5,5,8,8,8],[2,2,2,5,5,5,8,8,8],
#                 [3,3,3,6,6,6,9,9,9],[3,3,3,6,6,6,9,9,9],[3,3,3,6,6,6,9,9,9]])


def boxConversion(board):
    "Initialize an empty matrix"
    boxes = np.zeros((0,0),dtype = int)
    "first 3 columns at a time, because boxes are 3 columns wide"
    "So we must jump to the next 3 columns after each iteration"
    for column in range(0,9,3):
        "First 3 rows, because boxes are 3 rows tall"
        "So we must jump to the next 3 rows down"
        for row in range(0,9,3):
            "This Array will collect all the values in a box. Resetting here at empty"
            box_1 = np.array([],dtype=int)
            "We will now iterate down the matrix (play board) selecting 3 elements at a time..."
            "Starting at the top of each box and working down"
            for x in range(3):
                selection = board[x+row][column+0:column+3]
                box_1 = np.append(box_1,selection)
            "now append this collection array to the empty matrix" 
            boxes = np.append(boxes,box_1)
    
    "Reshape the matrix so that it sorts each 'boxes values' into the proper rows"
    boxes = boxes.reshape(9,9)
    return(boxes)


"Now that we have an algorithm for sorting each part we need to check into rows of a matrix, we "
"can start working on placing the random values and then checking"

def checkBox(board, box_no, value):

    box_matrix = boxConversion(board)
    
    for element in box_matrix[box_no-1]:
        if element == value:
            inRow = True
            break
        elif element != value:
            inRow = False
    return(inRow)
    

def checkColumn(board, column, value):
    column_matrix = board.transpose()
    for element in column_matrix[column]:
        if element == value:
            inRow = True
            break
        elif element != value:
            inRow = False
    return(inRow)
 

"Returns true if value is in the row"
def checkRow(board, row, value):
    for element in board[row]:
        if element == value:
            inRow = True
            break
        elif element != value:
            inRow = False
    return(inRow)
   

"Will Return which box I am searching currently"
def whichBox(row, column):
    if row == 0 or row == 1 or row == 2:
        if column == 0 or column == 1 or column == 2:
            box = 1
    if row == 0 or row == 1 or row == 2:
        if column == 3 or column == 4 or column == 5:
            box = 4
    if row == 0 or row == 1 or row == 2:
        if column == 6 or column == 7 or column  == 8:
            box = 7
        
    if row == 3 or row == 4 or row == 5:
        if column == 0 or column  == 1 or column  == 2:
            box = 2
    if row == 3 or row == 4 or row == 5:
        if column == 3 or column  == 4 or column  == 5:
            box = 5
    if row == 3 or row == 4 or row == 5:
        if column == 6 or column  == 7 or column  == 8:
            box = 8
            
    if row == 6 or row == 7 or row == 8:
        if column == 0 or column  == 1 or column  == 2:
            box = 3
    if row == 6 or row == 7 or row == 8:
        if column == 3 or column  == 4 or column  == 5:
            box = 6
    if row == 6 or row == 7 or row == 8:
        if column == 6 or column  == 7 or column  == 8:
            box = 9
    return(box)
            


'''################## What needs to Be done Next ##############
A comparison vector needs to be made to force a pick that has already been made 
in the last box. This way there will not be any conflicts
################################################################'''

"Pulls out number that is selected so now less to chose from with random and cant get same one" 
"twice"

"Need to keep track of available numbers in each box"
box_no = 0
boxes_filled = int(0)

for row in range(0,9):
    "Available Numbers to Append"
    numbers = np.arange(1,10,1)        
    
    for column in range(0,9):
        
        box_no = whichBox(row, column)
        
        "Need to compare available in box and row to avoid conflicts"
        valid_picks = np.intersect1d(numbers, available_box[box_no])
        placed = bool(False)
        
        while placed == False:
            "Chosing random value from numbers"
            
            value = random.choice(valid_picks)       

            allowed = False
            if checkRow(board, row, value) != True:
                allowed = True
                
            if allowed == True and checkColumn(board,column,value) == True:
                allowed = False
                
            if allowed == True and checkBox(board, box_no, value) == True:
                allowed = False
            
            if allowed == True:
                board[row,column] = value
                placed = True
            
            
        "Subtracting value from numbers" 
        
        numbers = numbers[numbers != value] 
        available_box[0] = np.where(available_box[0]!=value, available_box[0], 0)
        boxes_filled += 1
        
        print(boxes_filled)
        





   