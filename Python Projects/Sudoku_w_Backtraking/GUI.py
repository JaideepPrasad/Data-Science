import time
import pygame
pygame.font.init()

class GUI:
    def __init__(self, board, max_Attempts, window, refreshRate):
        self.board = board
        self.board_Len = len(board)
        self.max_Attempts = max_Attempts
        self.actual_Attempts = 0
        self.window = window
        self.refreshRate = refreshRate
  
    def draw(self):
        # Setting some constants
        width , height = 500, 500                       
        cell_size = width/9
        white = (255, 255, 255)	# rgb
        black = (0, 0, 0)		# rgb
        green = (0, 255, 0)     # rgb
        font = pygame.font.SysFont("comicsans", 40)
        empty_Cell = self.find_Empty()                # Find next empty cell

        self.window.fill(white)                       # Make the whole forground white so we don't have overlay when drawing numbers
        for i in range(self.board_Len):               # Go through each row and col so we can draw the cell lines
            for j in range(self.board_Len):
                if i%3 == 0 and i != 0:               # These if statements are to draw the thick lines that break the board into 9 smaller squares 
                    thickness = 4                     # We simply change the thickness of the line 
                else:
                    thickness = 1
                pygame.draw.line(self.window, black, (i, i*cell_size), (width, i*cell_size), thickness) # Draw the line (window, color, start point, end point, thickness)

                if j%3 == 0 and j != 0:
                    thickness = 4
                else:
                    thickness = 1
                pygame.draw.line(self.window, black, (j*cell_size, 0), (j*cell_size, height), thickness)

                if empty_Cell != None:                              # This is the highlight the cell that will change it's value
                    if i == empty_Cell[0] and j == empty_Cell[1]:   # When drawing our row/col, if the match with the empty cell we found
                        pygame.draw.rect(self.window, green, (j*cell_size, i*cell_size, cell_size, cell_size))    # Draw a square filling the cell (window, color, start point x, y, end point in reference from start point x, y)

                # Draw the value in the center of the cell
                value = self.board[j][i]                        # Capture value
                text = font.render(str(value), True, black)     # Decide what the text will be (str, visable, text color)
                textRect = text.get_rect()                      # Get the size of the text
                textRect.center = (i*cell_size + cell_size // 2, j*cell_size + cell_size // 2)  # Get the center of the text size
                self.window.blit(text, textRect)                # Draw in 'self.window' (what will you draw, where will you draw)

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

        # Check  if value fits in row
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
                self.draw()                                                             # Draw new board         
                pygame.display.update()                                                 # Update display with new board 
                time.sleep(self.refreshRate)                                            # Wait for 'n' number of sec (denoted by self.refreshRate), this is so we can see which cell is changing at a comfortable speed
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