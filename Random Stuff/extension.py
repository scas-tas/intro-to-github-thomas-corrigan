"""
A seating plan checker for a classroom. 
Scenario: Classroom Seating Plan
The 2D array is a 3×3 grid of student names. 
    1.Display — nested loop to print the grid row by row
    2.Count — find empty seats using a flattened comprehension
    3.Search — locate a student by name and return their row/column
Good discussion hooks for class:
    Use your intrinsic documentation  | row and col instead of i and j? (readability)
    How would you add a student to an empty seat? (introduces index assignment)
    What happens if you search for a name that doesn't exist?
    I wonder whether you can treat this like a stack. Why/Why not?
Easy to extend into OOP if you want to bridge into that unit : swap strings for Student objects
"""

grid = [
    ["","",""],
    ["","",""],
    ["","",""]
]


def showgrid():
    for grid1 in grid:
        print(grid1)

def addstudent():
    name = input("What is your name?: ")
    row = int(input("What Row do you want to sit in?: "))-1
    col = int(input("What Column do you want to sit in?: "))-1
    grid[row][col] = name


addstudent()
showgrid()
