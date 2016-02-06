class Solution:
    # @param {int[]} A an integer array
    # @return {int} an integer
    def stoneGame(self, A):
        # Write your code here
        # dp[i][j] is the min score from A[i:j+1]
        # got the state function wrong the first time, need to redo next time
        def search(i, j):
            if visited[i][j]:
                return dp[i][j]
            for k in xrange(i,j):
                dp[i][j] = min(dp[i][j], search(i, k)+search(k+1, j)+sumA[i][j]) #!!!! a traverse, not just left and right two situations
            visited[i][j] = True  #!!!typo: not visited(i, j)
            return dp[i][j]
        if not A:
            return 0
        n = len(A)
        dp = [[sys.maxint for i in xrange(n)] for j in xrange(n)]
        visited = [[False for i in xrange(n)] for j in xrange(n)]
        sumA = [[0 for i in xrange(n)] for j in xrange(n)] #!!!!shouldn't use dp[:]
        for i in xrange(n):
            sA = 0
            dp[i][i] = 0
            visited[i][i] = True
            for j in xrange(i, n): #!!!!!!!!!!!j is (i, n) not (0, n)
                sA += A[j]
                sumA[i][j] = sA
        search(0, n-1)
        return dp[0][n-1]
