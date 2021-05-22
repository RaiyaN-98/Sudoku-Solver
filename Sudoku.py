given_board = [
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

def fill(board, curr, empty_pos, maximum_num):
    if curr == maximum_num:
        return (True, board)
    
    flag = False
    for i in range(1,10):
        if is_valid(board, i, empty_pos[curr]):
            board[empty_pos[curr][0]][empty_pos[curr][1]] = i
            x = fill(board, curr+1, empty_pos, maximum_num)
            if x[0] == True:
                board = x[1]
                flag = True
                break
            else:
                board[empty_pos[curr][0]][empty_pos[curr][1]] = 0

    return (flag, board)

     

def solve(board):
    empty_pos = find_empty(board)
    maximum_num = len(empty_pos)
    val = fill(board, 0, empty_pos, maximum_num)
    print_board(val[1])



def is_valid(board, num, pos):
     
    #Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num:
            return False
     
    #Check coloum
    for i in range(len(board)):
        if board[i][pos[1]] == num:
            return False
    
    #Check square
    x = (pos[0]//3)*3
    y = (pos[1]//3)*3
    for i in range(3):
        for j in range(3):
            if board[x+i][y+j] == num:
                return False
    
    return True


def print_board(board):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("-----------------------") 
        
        for j in range(len(board[0])):
            if j%3 == 0 and j != 0:
                print(" | ", end="")
            if j == 0:
                print(board[i][j],end=" ")
            else:
                print(str(board[i][j]) + " ",end="")
            if j == len(board[0])-1:
                print(end="\n") 


def find_empty(board):
    x = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                x.append((i,j)) 
    return x 

print_board(given_board)
print("\nSolution: ")
solve(given_board)