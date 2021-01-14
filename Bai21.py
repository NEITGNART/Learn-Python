
def solve():

    a = [0] * 100
    visited = [False] * 100
    s = []
    s.append('A')
    s.append('B')
    s.append('C')
    n = len(s)
    def Try(i: int):

        for j in range(1, n + 1):
            if (visited[j] is not True):
                a[i] = j
                visited[j] = True
                if (i == n):
                    for i in range(1, n + 1):
                        print(str(s[a[i] - 1]) + ' ', end = '')
                    print('\n', end = '')
                else:
                    Try(i + 1)
                visited[j] = False

    Try(1)

def main():
    solve()


if '__main__' == __name__:
    main()
