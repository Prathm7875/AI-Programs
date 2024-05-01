def main():
    N = int(input("Enter No of Queens: "))
    board = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            board[i][j] = 0

    if helper(board, 0, N):
        print_board(board, N)
    else:
        print("Solution does not exist")

def helper(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if safe(board, col, i, N):
            board[i][col] = 1
            if helper(board, col + 1, N):
                return True
            board[i][col] = 0

    return False

def safe(board, col, row, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def print_board(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print(" Q ", end=" ")
            else:
                print(" _ ", end=" ")
        print()

if __name__ == "__main__":
    main()

# Output :
# Enter No of Queens: 5
#  Q   _   _   _   _  
#  _   _   _   Q   _  
#  _   Q   _   _   _  
#  _   _   _   _   Q  
#  _   _   Q   _   _ 
