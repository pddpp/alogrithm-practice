class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        # write your code here
        # need to review and think about initialization, state function myself
        # dp[i][j][m] is select j element from the first i element(A[:i]), if the sum can be m
        # !!!be careful what the return is
        # be carefult about i, i-1 or i+1 everywhere, don't go out of range!
        # need to initial dp[i][0][0]!!!!
        result = 0
        n = len(A)
        dp = [[[0 for i in xrange(target+1)] for j in xrange(k+1)] for l in xrange(n+1)]
        for i in xrange(n):
            dp[i][0][0] = 1
        for i in xrange(1, n+1):
            for j in xrange(1, k+1):
                for m in xrange(target+1):
                    dp[i][j][m] = dp[i-1][j][m]
                    if m >= A[i-1]: #!!! need this
                       dp[i][j][m] += dp[i-1][j-1][m-A[i-1]]
        return dp[n][k][target]
