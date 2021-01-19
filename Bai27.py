def staircase(n, m):
  # Your code goes here
  dp = [0] * (n + 1)
  dp[0] = 1

  for i in range(1, n + 1):
    for j in range(0, m + 1):
      if (i - j >= 0):
        dp[i] += dp[i - j]

  return dp[n]

''' Trick with python. Another way python bring powerful tools '''

import sys
sys.setrecursionlimit(5000)
from functools import lru_cache
@lru_cache(maxsize = None)
def staircase(n, m):
  # base case of when there is no stair
  if n == 0:    
    return 1
  ways = 0
  # iterate over number of steps, we can take
  for i in range(1,m+1):  
    # if steps remaining is smaller than the jump step, skip   
    if i <= n:  
      # recursive call with n i units lesser where i is the number of steps taken here            
      ways += staircase(n-i, m) 
  return ways

print(staircase(1500,6)) # this number produce a huge of solution
