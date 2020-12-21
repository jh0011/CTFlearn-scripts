#CTFlearn
#Medium challenge 434 (Dawn's Lawn)
"""
To count the number of flowers after mowing and growing. 
"""


# Global variables (lawn_size && overall_lawn)
lawn_size = 20

dataFile = open('C:\\Users\\dell\\Downloads\\dawn2.txt')
fileLines = dataFile.readlines()

# Create a 2D array with numbers representing each character instead
overall_lawn = [[0 for i in range (lawn_size)] for j in range(lawn_size)]
lawn_ID = [[0] * lawn_size] * lawn_size
row_count = -1
col_count = -1
for line in fileLines:
    row_count = row_count + 1
    col_count = -1
    for character in line:
        col_count = col_count + 1
        if character == '*': # Flower
            overall_lawn[row_count][col_count] = 6
        elif character == '|': # Grass 4
            overall_lawn[row_count][col_count] = 5
        elif character == '/': # Grass 3
            overall_lawn[row_count][col_count] = 4
        elif character == '-': # Grass 2
            overall_lawn[row_count][col_count] = 3
        elif character == '\\': # Grass 1
            overall_lawn[row_count][col_count] = 2
        elif character == '_': # Fertile dirt
            overall_lawn[row_count][col_count] = 1
        elif character == '.': # Infertile dirt
            overall_lawn[row_count][col_count] = 0
        else:
            print("Unknown Character")

# Verify the initial lawn
print("Initial Lawn: ", overall_lawn)

# This is how the lawn mower moves. 
# Down - when the col_count is divisible by 2.
# Up - when the col_count is not divisible by 2.       
def lawn_mower_movement():
    count_growth = 0
    for col in range(lawn_size):
        if (col % 2 == 0):
            for row in range(lawn_size):
                mowed_lawn(row, col)
                count_growth = count_growth + 1
                if (count_growth > lawn_size):
                    pick_lawn_growth(row, col, count_growth)
        else:
            for row in range(lawn_size - 1, -1, -1):
                mowed_lawn(row, col)
                count_growth = count_growth + 1
                if (count_growth > lawn_size):
                    pick_lawn_growth(row, col, count_growth)
    
# The tile value is decremented when that tile is mowed
def mowed_lawn(row, col):
    if (overall_lawn[row][col] <= 2):
        overall_lawn[row][col] = 0
    else:
        overall_lawn[row][col] = overall_lawn[row][col] - 2

# To pick which of the previous tiles are growing.
# Growth happens every 20 iterations.
def pick_lawn_growth(row, col, count_growth):
    for x in range(0, col, 1): # Consider all the previous cols
        if x % 2 == 0:
            lawn_growth((count_growth - 1) % 20, x) # Grow from index 0
        else:
            lawn_growth((lawn_size - 1) - (count_growth - 1) % 20, x) # Grow from index 19

# The tile value is incremented during the growth
def lawn_growth(row, col):
    if (overall_lawn[row][col] == 6):
        overall_lawn[row][col] = 6
    elif (overall_lawn[row][col] == 0):
        overall_lawn[row][col] = 0
    else:
        overall_lawn[row][col] = overall_lawn[row][col] + 1

# To count a certain type of tile.
# Pass in 6 as the parameter for flowers
def count_type(value):
    countVal = 0
    for row in overall_lawn:
        for col in row:
            if col == value:
                countVal = countVal + 1
    return countVal




lawn_mower_movement()
# Verify the final lawn
print("Final lawn: ", overall_lawn)
print("Number of flowers: ", count_type(6))