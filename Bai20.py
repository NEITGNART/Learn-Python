
def solve():
    A = list(map(int, input().split()))
    n = len(A)
    grid = [[0 for x in range(n + 1)] for y in range(n + 1)]

    for i in range(n):
        grid[0][i] = A[i]



    for i in range(1, n):
        for j in range(n):
            grid[i][j] = grid[i-1][j] + grid[i-1][j+1]

    col = 1

    for i in range(n - 1, -1, -1):
        print('[' , end = '')
        j = col
        temp = 0
        while (j - 1):
            print(str(grid[i][temp]) + ' ', end = "")
            temp += 1
            j -= 1
        print(str(grid[i][temp]), end = '')
        print( ']' + '\n', end = '')
        col += 1


def main():
    solve()


if '__main__' == __name__:
    main()
