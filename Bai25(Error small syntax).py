import sys
def solve(a : list, n : int, k : int):

    sum_ = sum(a)
    sum_partition = sum_ // k
    if sum_ % k != 0:
        return False

    visited = [False] * (n + 5)
    ok = False
    temp = False
    def Try(s : list, i : int, ok : bool):

        #in pratice, remember that utilize the ok variable to optimize the time complexity (Prune)  if ok == True return

        if i == k:
            print("Had found solution")
            sys.exit()
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

    temp = False
    Try(0, 0, temp)
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
