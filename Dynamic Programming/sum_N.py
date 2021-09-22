#problem: Find sum of first N numbers

def funcNSum(n):
    dp = [0]*(n+1)
    dp[0]= 0
    for i in range(1,n+1):
        dp[i] = i+dp[i-1]
    return dp[-1]

#driver code:
n = 5
print("Sum of first",n,"numbers is:",funcNSum(n))