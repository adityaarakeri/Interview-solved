# https://www.geeksforgeeks.org/n-queen-in-on-space/

# print the solutions for the queen to travel on chess board
# also print the steps by count on the board
# Contribution made by "gitkp" 



n = 8

def issafe(n, x, y, sol):
    if (x >= 0 and x < n and y >= 0 and y < n and sol[x][y] == -1):
        return True
    return False

def printsol(sol, n):
    for i in range(n):
        for j in range(n):
            print(sol[i][j], end=' ')
        print()

def move1(n, x, y, steps, x_move, y_move, sol):
    if (steps == n * n):
        return True

    for i in range(n):
        nxtx = x + x_move[i]
        nxty = y + y_move[i]

        if (issafe(n, nxtx, nxty, sol)):
            sol[nxtx][nxty]= steps
            if (move1(n, nxtx, nxty, steps+1, x_move, y_move, sol)):
                return True
            
            sol[nxtx][nxty] = -1
    
    return False

def solve(n):
    sol = [[-1 for _ in range(n)] for _ in range(n)]

    x_move = [1,2,2,1,-1,-2,-2,-1]
    y_move = [2,1,-1,-2,-2,-1,1,2]

    sol[0][0] = 0

    steps = 1
    if (not move1(n, 0, 0, steps, x_move, y_move, sol)):
        print("No solution")
    else:
        printsol(sol, n)

if __name__ == "__main__":
    solve(n)
    
