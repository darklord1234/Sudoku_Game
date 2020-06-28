

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")

def find_empty(b):
    """Gives position of first available empty position"""
    for i in range(len(b)):
        for j in range(len(b)):
            if b[i][j] == 0:
                return (i, j)
    return None

def is_valid(b, num, pos):
    """checks given number is valid for that position based on rowas and column"""

    # Check Row
    if num in b[pos[0]]:
        return False

    # Check Column
    for i in range(len(b)):
        if b[i][pos[1]] == num:
            return False
    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if b[i][j] == num:
                return False
    return True

def solve(b):
    f = find_empty(b)
    if not f:
        return True
    else:
        row, col = f
    for i in range(1, 10):
        if is_valid(b, i, (row, col)):
            b[row][col] = i

            if solve(b):
                return True
            b[row][col] = 0

    return False

print_board(board)
solve(board)
print("+++++++++++++++++++++++++++++++++++++")
print_board(board)
