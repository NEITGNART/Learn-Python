
def solve(a : list, n : int, k : int):

    sum_ = sum(a)
    sum_partition = sum_ // k
    if sum_ % k != 0:
        return False

    visited = [False] * (n + 5)

    def Try(s, i, ok):

        if (ok == True):
            return
        if i == k:
            ok = True
            print("Has solution")
            return
        for j in range(n):
            if visited[j] is False:
                visited[j] = True
                if (s == sum_partition):
                    Try(0, i + 1, ok)
                if s > sum_partition:
                    return False
                else:
                    Try(s + a[j], i, ok)
            visited[j] = False

    ok = False
    Try(0, 0, ok)
    return ok

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        k = int(input())
        a = list(map(int, input().split()))
        if (solve(a, n, k) == True):
            pass
        else:
            print("No solution")


if __name__ == '__main__':
    main()
