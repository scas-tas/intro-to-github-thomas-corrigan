import random as rand

def randnumber():
    return rand.randint(0,4)


num = int(input("How many X's: "))

grid = [
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ']
]

for row in range(num):
    row = randnumber()
    col = randnumber()
    grid[row][col] = "X"

for grid1 in grid:
    print(grid1)

