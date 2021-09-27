"""
Unique Paths
	A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
	The robot can only move either down or right at any point in time.
	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
	How many possible unique paths are there?
	+---+---+---+---+
	| S |   |   |   |
	+---+---+---+---+
	|   |   |   |   |
	+---+---+---+---+
	|   |   |   | E |
	+---+---+---+---+
	Above is a 3 x 4 grid. How many possible unique paths are there?
"""

def noWays(m,n):
    dp = [[0 for j in range(n)] for i in range(m)]
    dp[0][0] = 1
    for i in range(0, m):
        for j in range(0, n):
            if i > 0 and j > 0:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
            elif i > 0:
                dp[i][j] = dp[i - 1][j]
            elif j > 0:
                dp[i][j] = dp[i][j - 1]
    return dp[m - 1][n - 1]

if __name__ == "__main__":
    m = 3
    n = 2
    ans = noWays(m,n)
    print(ans)