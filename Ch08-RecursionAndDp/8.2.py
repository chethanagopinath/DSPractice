'''
consider all cells to have True or False values - so following the cells 
with True would eventually lead us to the end of the maze/solution?
Like a 2D list of False and True values

in main fn 
- do some error checking
- call helper recursive function

in recursive fn
- base cases - when should my solution give me definitive values or when we stop recursing?
    - if we go out of bounds or the current cell is False => return False
- have a Boolean check if we are the origin and hold the value of (row == 0 and col == 0)
- recursive cases - which cells if they returned True would help me get to grid[r][c]?
    - if the cell was the origin or
    - if the cell above current was True (grid[r-1][c]) or 
    - if the cell to the left was True (grid[r][c-1]) 
    we create point = [r, c] and append this point to the path 
    and return True 
'''
def path_finder()
