#a person can take a max jump of k steps
#k is user input

def climbStair(n,k):
    dp = [0]*(n+1)
    dp[0] = dp[1] = 1
    for i in range(2,n+1):
        #f(n) = f(n-1)+f(n-2)+....+f(n-k)
        for j in range(1,k+1):
            if i-j < 0:
                #ignore
                continue
            dp[i] += dp[i-j]
    return dp[-1]

#driver code:
n = 5
k = 3
print("No of ways possible to reach level",n,"is:",climbStair(n,k))


#time-complexity is O(nk)
#space-complexity is O(n)