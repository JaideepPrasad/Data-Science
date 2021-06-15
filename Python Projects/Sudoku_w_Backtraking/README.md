# Sudoku Solver with Backtracking
___
 
## Project Goal

The goal of this project is to create a visualization for a sudoku solver using backtracking as a warm up into python programming. The code should be able to solve the sudoku board using either the terminal or using a visualization. There are 3 python files, Main, GUI and Sudoku. The Main.py file is what the user will be using to run the code. There is a variable called board where you can add your own board. At the very bottom you will see "Visual()" to run the GUI verion of the code and "Puzzel()" to run the terminal version of the code, comment out the option you DON"T WANT.

## Process

Main:
   - Input sudoku board (there is a link above for free online sudoku boards with solutions if you like)
   - Call the terminal solver and cap the solver attempts/steps at 500 that way if the board is unsolvable, we don't run in an infinate loop
   - Call the GUI solver
      - set up window for the solver
      - call GUI solver with 500 attempts and an visual update speed of 0.5 seconds
      - 'display everything' loop
 
For the most part the terminal solver (Sudoku.py) and visual solver (GUI.py) are the same so I will breifly explain whats going on with both of them:
   - Display board (print_board/draw method)
   - Find next empty cell denoted by '0'
      - have a nested forloop to search every cell to see if it's 0
      - if so, break and return the location
   - Verify potential numbers in empty cell
      - check row values by iterating over them to see if a number occurs twice
      - check column values by iterating over them to see if a number occurs twice
      - break the board up into the 9 squares, iterate over the cells to see if a number ouccurs twice
   - Solver
      -  we call the method to find an empty cell
      -  we run through all possible values to through the verify function to check which number fits
      -  if the number we chose fits, we will put our number in the empty cell and run the solver again.
         - in early iterations this won't do much but in later iterations, this makes sure we don't use the same number multiple times despite the number being a valid solution
         - this is where the backtracking comes in
      - we check to see if we went over the max attempts we gave the solver
      - assuming we could not find the correct valid answer, we keep the empty cell empty.     
    

## Results

The results are good, expecially this being the first time I used pygames. Below you will see a gif of the visual solver (GUI.py) and am image of the final few steps of the terminal solver (Sudoku.py).

Visual Solver (GUI.py):

![ezgif com-gif-maker (1) (1)](https://user-images.githubusercontent.com/32663193/122104277-835c4800-cde5-11eb-9a6c-8b91779e3a8e.gif)

Terminal Solver (Sudoku.py):

![Capture](https://user-images.githubusercontent.com/32663193/122104342-940cbe00-cde5-11eb-9bc1-c8eb48566b28.PNG)


## Issues

1) The close window button for the GUI solver doesn't work
