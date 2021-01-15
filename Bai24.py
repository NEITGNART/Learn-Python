
def solve(set, n, sum):
    dp = [[False for i in range(sum + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, sum + 1):
        dp[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < set[i - 1]:
                dp[i][j] = dp[i - 1][j]
            elif j >= set[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - set[i - 1]]

    return dp[n][sum]


def main():

    # 7 3 2 5 8
    # 14
    set = list(map(int, input().split()))
    sum = int(input())
    n = len(set)
    if (solve(set, n, sum) is True):
        print("Found")
    else:
        print("No subset with the given sum")


if __name__ == '__main__':
    main()
