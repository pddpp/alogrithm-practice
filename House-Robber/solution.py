class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        # Easy dp problem, implemented with rolling array
        if not A:
            return 0
        if len(A) == 1:
            return A[0]
        dp = [0, 0]
        dp[0] = A[0]
        dp[1] = A[1]
        for i in xrange(2, len(A)):
            dp[i%2] = max(dp[(i-1)%2], dp[(i-2)%2]+A[i])
        return dp[(len(A)-1)%2] #!! need to %2 as well
