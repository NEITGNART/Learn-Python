
def solve():

    n = int(input())

    grid = [[int(0) for i in range(n + 1)] for j in range(n + 1)]
    for x in range(n):
        grid[x] = list(map(int, input().split()))
    ok = [[False for i in range(n + 1)] for j in range(n + 1)]

    # 4
    # 1 0 0 0
    # 1 1 0 1
    # 0 1 0 0
    # 1 1 1 1

    # 5
    # 1 0 0 0 0
    # 1 1 1 1 1
    # 1 1 0 0 1
    # 0 1 1 1 1
    # 0 0 0 1 1

    res = []
    currentX = 1
    currentY = 1

    # robot can find the path from the current position to the most right down corner with multiple solution


    def Try(i: int, j: int, s:str):

        if (i < 0 or i >= n or j < 0 or j >= n or grid[i][j] == 0):
            return

        if (i == n - 1 and j == n - 1 and grid[i][j] == 1):
           res.append(s)
           s = '' # clear string s

        if (0 < i + 1 < n and ok[i + 1][j] == False and grid[i+1][j] == 1):
            ok[i+1][j] = True
            Try(i + 1, j, s + "D")
            ok[i+1][j] = False

        if (0 < j + 1 < n and ok[i][j+1] == False and grid[i][j + 1] == 1):
            ok[i][j+1] = True
            Try(i, j + 1, s + "R")
            ok[i][j+1] = False

        if (0 <= j - 1 < n and ok[i][j-1] == False and grid[i][j-1] == 1):
            ok[i][j-1] = True
            Try(i, j-1, s + "L")
            ok[i][j-1] = False

        if (0 <= i - 1 < n and ok[i-1][j] == False and grid[i - 1][j] == 1):
            ok[i-1][j] = True
            Try(i-1, j, s + "U")
            ok[i-1][j] = False


    if (grid[currentX][currentY] == 1):
        ok[currentX][currentY] = True
        Try(currentX, currentY, '')
        for x in res:
            print(x)
    else:
        print("No solution")




def main():
    solve()


if '__main__' == __name__:
    main()
