#https://www.youtube.com/watch?v=hekG82t4U_M&t=75s&ab_channel=AndreyGrehov
#paid staircase. It takes n staircases to reach the top and you have to pay arr[i] to step
#on the i-th stair. At max you take a jump of 2 steps. Find the min cost


def minCostclimbStair(n,arr):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = arr[1]
    for i in range(2,n+1):
        dp[i] = arr[i] + min(dp[i-1],dp[i-2])
    return min(dp[-1],dp[-2]) #or dp[n]

#driver code:
n = 3
arr = [0,10,15,20]
print("Min cost to reach level",n,"is:",minCostclimbStair(n,arr))