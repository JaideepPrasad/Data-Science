import pygame

class Sudoku:
    def __init__(self, board, max_Attempts):
        self.board = board
        self.board_Len = len(board)
        self.max_Attempts = max_Attempts
        self.actual_Attempts = 0

    def print_Board(self):
        for row in range(self.board_Len):
            if row%3 == 0:
                print("---------------------")
            for column in range(self.board_Len):
                if column == 0 or column%3 == 0:
                    print("|", end="")
                    print(self.board[row][column], end="")
                    print(" ",end="")
                elif column == 8:
                    print(self.board[row][column], end="")
                    print("|")
                else:
                    print(self.board[row][column], end="")
                    print(" ",end="")

    def find_Empty(self):                               # Find next empty cell
        for row in range(self.board_Len):               # Look through every row
            for column in range(self.board_Len):        # Look through every column
                if self.board[row][column] == 0:        # If the value at row,column = 0
                    empty_Cell = [row, column]          # We save the coordinate of that cell
                    break                               # We stop looking at each column
                else:
                    empty_Cell = None                   # If we don't find 0, empty_Cell will be None
            if empty_Cell != None:                      # After looking through each column, if empty_Cell is not None,
                break                                   # we stop looking at each row
        if empty_Cell != None:
            print (f"Empty Cell: [{empty_Cell[0]},{empty_Cell[1]}]")
        else:
            print (f"Empty Cell is NONE")
        return empty_Cell                               

    def verify_if_number_is_a_possible_fit(self, number, empty_Cell):
        row = empty_Cell[0]
        column = empty_Cell[1]

        # Check if value fits in row
        for x in range(self.board_Len):   
            if self.board[row][x] == number and self.board[empty_Cell[0]][empty_Cell[1]] != number:
                return False
        
        # Check if value fits in col
        for x in range(self.board_Len):
            if self.board[x][column] == number and self.board[empty_Cell[0]][empty_Cell[1]] != number:
                return False
        
        # Check if value fits in square
        squareRow = row//3
        squareColumn = column//3

        for x in range(squareRow*3, squareRow*3 +3):
            for y in range(squareColumn*3, squareColumn*3 + 3):
                if self.board[x][y] == number and self.board[empty_Cell[0]][empty_Cell[1]] != number:
                    return False

        return True
    
    def solve(self):
        empty_Cell = self.find_Empty()
        if empty_Cell == None:
            return True

        for number in range(1, 10):
            possibleFit = self.verify_if_number_is_a_possible_fit(number, empty_Cell)   # Check to see if number from 1-9 is a possible fit
            if possibleFit == True:                                                     # If it's a possible fit
                self.board[empty_Cell[0]][empty_Cell[1]] = number                       # Replace the 0 on the board with number
                self.print_Board()                                                      # Print new board
                solved = self.solve()                                                   # Recurssivly check for other possible solutions branching off this possibility
                if  solved == True:                                                     # If we cant find any empty_Cell
                    return True                                                         # We solved the board
                else:                                                                   # If we do find an empty_Cell
                    continue
        
        self.actual_Attempts = self.actual_Attempts + 1                                 # We keep a counter of how many times the program backtracked
        
        if self.actual_Attempts > self.max_Attempts:                                    # We also give the program a max number of tries. 
            print("Could not solve")                                                    # In the case we have an unsolvable board, after a large number of tries (that we choose) the program ends itself
            return True                                                                 # This is to avoid an infinate loop, or to address an unsolvable board
        
        self.board[empty_Cell[0]][empty_Cell[1]] = 0                                    # If current empty cell does not lead to next empty cell possible valid value, we set current empty cell to 0, and go to previous empty cell
        return False