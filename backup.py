#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:06:59 2021

@author: dillon
"""
import numpy as np
import random

board = np.array([[1,2,1,4,5,3,7,8,7],[1,1,1,4,4,4,7,7,7],[1,1,1,4,4,4,7,7,7],
                [2,2,2,5,5,5,8,8,8],[2,2,2,5,5,5,8,8,8],[2,2,2,5,5,5,8,8,8],
                 [3,3,3,6,6,6,9,9,9],[3,3,3,6,6,6,9,9,9],[3,3,3,6,6,6,9,9,9]])
numbers = np.arange(1,10,1)
value = random.choice(numbers)
print(value)
print(board)
row = random.choice(numbers)
print("row")
print(row)

'''
print(board[0])
for element in board[0]:
    if element == 5:
        print("No good")
    elif element != 5:
        print("winner winner chicken dinner")
     '''   
        
def checkRow(row_matrix, row, value): 
    for element in row_matrix[row]:
        if element == value:
            inRow = True
            break
        elif element != value:
            inRow = False
    return(inRow)
    
print(checkRow(board,row,value))

def checkColumn(board, column):
    column_matrix = board.transpose()
    for element in column_matrix[column]:
        if element == value:
            inRow = True
            break
        elif element != value:
            inRow = False
    return(inRow)
