#a person can take a max jump of 3 steps
#no of stairs can be climbed is either 1 or 2
#find no of ways to possible to reach top

def climbStair(n):
    dp = [0]*(n+1)
    dp[0] = dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp[-1]

#driver code:
n = 5
print("No of ways possible to reach level",n,"is:",climbStair(n))


#time-complexity is O(n)
#space-complexity is O(n)