def staircase(n, m):
  # Your code goes here
  dp = [0] * (n + 1)
  dp[0] = 1

  for i in range(1, n + 1):
    for j in range(0, m + 1):
      if (i - j >= 0):
        dp[i] += dp[i - j]

  return dp[n]

stressTesting = True
