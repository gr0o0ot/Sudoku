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

def solve(mat):
    find = find_emptybox(mat)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid_board(mat, i, (row, col)):
            mat[row][col] = i

            if solve(mat):
                return True

            mat[row][col] = 0
    return False


def valid_board(mat, num, pos):
    # checking  row
    for i in range(len(mat[0])):
        if mat[pos[0]][i] == num and pos[1] != i:
            return False
    # checking column
    for i in range(len(mat[0])):
        if  mat[i][pos[1] ] == num and pos[0] != i:
            return False
    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3,box_y*3 + 3):
        for j in range(box_x*3,box_x*3 + 3):
            if mat[i][j] == num and (i, j) != pos:
                return False

    return True
# grid


def print_board(mat):
    for i in range(len(mat)):
        if i % 3 == 0 and i != 0:
            print(30*"-")
        for j  in range(len(mat[0])):
            if j % 3 ==0 and j != 0:
                print(" | ", end ="")

            if  j == 8:
                print(mat[i][j])
            else:
                print(str(mat[i][j]) + " ", end = "")

# print_board(board)


def find_emptybox(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 0:
                 return  ( i, j )  #row , column
    return None

print_board(board)
solve(board)
print("------------------------------------------------------")
print_board(board)

