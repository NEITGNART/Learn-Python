
def solve():
    A = list(map(int, input().split()))
    n = len(A)
    grid = [[0 for x in range(n + 1)] for y in range(n + 1)]

    for i in range(n):
        grid[0][i] = A[i]

    col = n

    for i in range(1, n):
        for j in range(col):
            grid[i][j] = grid[i-1][j] + grid[i-1][j+1]

    for i in range(n):
        print('[', end = '')
        for j in range(col - 1):
            print(str(grid[i][j]) + ',', end = '')
        print(grid[i][col-1], end = '')
        print(']', end = '')
        col -= 1
        print('\n', end = '')


def main():
    solve()


if '__main__' == __name__:
    main()
