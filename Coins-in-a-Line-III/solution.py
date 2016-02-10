class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        # dp[i][j] the max value that first player can get with coins [i:j+1] left
        # idea based on coins in a line(memorial search), code with minor typo
        def search(i, j):
            if visited[i][j]:
                return dp[i][j]
            if i < j:
                dp[i][j] = max(values[i]+min(search(i+2, j), search(i+1, j-1)), \
                               values[j]+min(search(i+1, j-1), search(i, j-2)))
            visited[i][j] = True
            return dp[i][j]
            
        n = len(values)
        dp = [[0 for i in xrange(n)] for j in xrange(n)]
        visited = [[False for i in xrange(n)] for j in xrange(n)]
        total = 0
        for i in xrange(n):
            dp[i][i] = values[i]
            total += values[i]
            visited[i][i] = True #!!! typo: visited[i][j]
            if i != n-1:
                dp[i][i+1] = max(values[i], values[i+1])
                visited[i][i+1] = True
        return search(0,n-1) > total/2
