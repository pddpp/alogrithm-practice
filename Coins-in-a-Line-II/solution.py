class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        # dp function almost got by myself, coded with minor typo.
        if not values:
            return False
        if len(values) <= 2:
            return True
        dp = [0 for i in xrange(len(values)+1)]
        dp[1] = values[-1]
        dp[2] = values[-1]+values[-2]
        dp[3] = values[-2]+values[-3]
        sum = values[0]+values[1]+values[2]
        for i in xrange(4, len(values)+1):
            sum += values[i-1]
            dp[i] = max(min(dp[i-2], dp[i-3])+values[len(values)-i], \
                        min(dp[i-3], dp[i-4])+values[len(values)-i]+values[len(values)-i+1]) #!![len(values)-i+1]
        return dp[len(values)] > sum/2
