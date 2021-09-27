"""
Problem:
	Maximum Profit in a Grid
	A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
	The robot can only move either down or right at any point in time.
	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
	Each cell contains a coin the robot can collect.
	What is the maximum profit the robot can accumulate?
	+---+---+---+---+
	| S | 2 | 2 | 1 |
	+---+---+---+---+
	| 3 | 1 | 1 | 1 |
	+---+---+---+---+
	| 4 | 4 | 2 | E |
	+---+---+---+---+
"""
def maxProf(arr):
    rows = len(arr)
    cols = len(arr[0])
    dp = [[0 for i in range(cols)] for j in range(rows)]
    dp[0][0] = arr[0][0]
    for i in range(0, rows):
        for j in range(0, cols):
            if i > 0 and j > 0:
                dp[i][j] = max(dp[i][j - 1] , dp[i - 1][j]) + arr[i][j]
            elif i > 0:
                dp[i][j] = dp[i - 1][j] + arr[i][j]
            elif j > 0:
                dp[i][j] = dp[i][j - 1] + arr[i][j]
    return dp[rows - 1][cols - 1]

if __name__ == '__main__':
    arr = [[1,2,2,50],[3,1,1,100],[4,4,2,0]]
    ans = maxProf(arr)
    print(ans)