#no of stairs can be climbed is either 1 or 2
#find no of ways to possible to reach top
#with reduced space complexity


def climbStair(n):
    #dp = [0]*(n+1)
    #dp[0] = dp[1] = 1
    a = b = 1
    for i in range(2,n+1):
        #dp[i] = dp[i-1]+dp[i-2]
        c = a+b
        a = b
        b = c
    #return dp[-1]
    return c

#driver code:
n = 5
print("No of ways possible to reach level",n,"is:",climbStair(n))


#time-complexity is O(n)
#space-complexity is O(1)