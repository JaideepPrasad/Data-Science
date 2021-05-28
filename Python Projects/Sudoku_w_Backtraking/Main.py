from Sudoku import Sudoku
from GUI import GUI
import pygame

# Sudoku puzzels with solutions can be found here:
# https://www.puzzles.ca/sudoku/

Board = [                               # '0' is an empty spot
        [1, 3, 0, 2, 0, 0, 7, 4, 0],    # Row 1
        [0, 2, 5, 0, 1, 0, 0, 0, 0],    # Row 2
        [4, 8, 0, 0, 6, 0, 0, 5, 0],    # so on
        [0, 0, 0, 7, 8, 0, 2, 1, 0],
        [5, 0, 0, 0, 9, 0, 3, 7, 0],
        [9, 0, 0, 0, 3, 0, 0, 0, 5],
        [0, 4, 0, 0, 0, 6, 8, 9, 0],
        [0, 5, 3, 0, 0, 1, 4, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

def Puzzle():
        sudoku = Sudoku(Board, 500)             # The number in the bracket is the max amount of tries, default is 500.
        print("Input Board:")
        sudoku.print_Board()
        print("****************************")
        sudoku.solve()
        print("****************************")
        print("Output Board:")
        sudoku.print_Board()

def Visual():  
        width , height = 500, 500                               # Width and hieght of out pygame window, if you change this, change it in GUI.draw too

        window = pygame.display.set_mode((width, height))       # Creating window
        pygame.display.set_caption("Sudoku Visulization")       # Creating window name

        gui = GUI(Board, 500, window, 0.5)                      # (Sudoku board, backtracking attempts, don't touch window, solving speed)

        run = True
        while run:                                              # Our 'game loop' as reference in pygame's documentation
                gui.solve()                                     
                gui.draw()
                pygame.display.update()

                for event in pygame.event.get():                # If we press the 'red X' button to close the window, we stop the loop
                        if event.type == pygame.QUIT:           
                                run = False

        pygame.quit()

Visual()                                                        # For the visual solver
#Puzzle()                                                       # For non-visual solver