class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        # First gaming question idea got from lecture, one time pass despite corner case
        if n == 0: #!!
            return False
        dp = [True, True, False, True]
        for i in xrange(4,n):
            dp[i%4] = (dp[(i-2)%4] and dp[(i-3)%4]) or (dp[(i-3)%4] and dp[(i-4)%4])
        return dp[(n-1)%4]
