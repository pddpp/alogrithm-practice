class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    # backpack problem, need to consider the sum < target case and the target already reached case
    def backPack(self, m, A):
        # write your code here
        # dp[i][j] is if we could use i stones to fill backpack j 
        total = 0
        for i in xrange(len(A)):
            total += A[i]
        if total <= m: #!!! early break: sum < target
            return total
        dp = [[False for i in xrange(m+1)] for j in xrange(2)]
        dp[0][0] = True
        dp[1][0] = True

        for i in xrange(1, len(A)+1):
            for j in xrange(1, m+1):
                dp[i%2][j] = dp[(i-1)%2][j]
                if j-A[i-1] >= 0:
                    dp[i%2][j] = dp[(i-1)%2][j-A[i-1]] or dp[(i-1)%2][j]
            if dp[i%2][m]: # early break: target already reached
                return m
        for i in reversed(xrange(m+1)):
            if dp[(len(A))%2][i]:
                return i
        return 0
