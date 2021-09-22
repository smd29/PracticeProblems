# paid staircase. It takes n staircases to reach the top and you have to pay arr[i] to step
# on the i-th stair. At max you take a jump of 2 steps. Find the min cost path


def minCostclimbStair(n, arr):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = arr[1]
    path = [0] * (n + 1)
    path[0] = path[1] = 0  # both 0th and 1st stair are climbed from 0th stair only
    for i in range(2, n + 1):
        dp[i] = arr[i] + min(dp[i - 1], dp[i - 2])
        path[i] = i - 1 if dp[i - 1] < dp[i - 2] else i - 2
    # return min(dp[-1],dp[-2]) #or dp[n]
    # path is having the details of how the top can be reached
    # [0, 0, 0, 2, 2, 3, 5, 5, 6]
    optimal_path = [0]
    i = len(path) - 1
    while i > 0:
        print(i)
        print("prev",path[i])
        optimal_path.insert(1,i)
        i = path[i]
    return optimal_path

# driver code:
n = 8
arr = [0, 3, 2, 4, 6, 1, 1, 5, 3]
print("Min cost to reach level", n, "is:", minCostclimbStair(n, arr))
