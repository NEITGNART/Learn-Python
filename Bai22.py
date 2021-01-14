
def solve():

    n = int(input())

    grid = [[int(0) for i in range(n + 1)] for j in range(n + 1)]
    for x in range(n):
        grid[x] = list(map(int, input().split()))
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


    # Start from the most left corner and destination is the most right down corner
    # Because each step robot move down or right. Thus as it can't collision, doesn't need a list bool

    res = []


    def Try(i: int, j: int, s:str):

        if (i < 0 or i >= n or j < 0 or j >= n or grid[i][j] == 0):
            return

        if (i == n - 1 and j == n - 1 and grid[i][j] == 1):
           res.append(s)
           s = '' # clear string s

        if (i + 1 < n and grid[i+1][j] == 1):
            Try(i + 1, j, s + "D")
        if (j + 1 < n and grid[i][j + 1] == 1):
            Try(i, j + 1, s + "R")

    if (grid[0][0] == 1):
        Try(0, 0, '')
        for x in res:
            print(x)
    else:
        print("No solution")

def main():
    solve()


if '__main__' == __name__:
    main()
