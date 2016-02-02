class Solution:
    """
    @param k: an integer
    @param prices: a list of integer
    @return: an integer which is maximum profit
    """
    def maxProfit(self, k, prices):
        # write your code here
        # hard question, not easy to get the correct state function, and need to thinking about many corner cases, redo it!
        def gain(buy_date, sell_date):
            return prices[sell_date]-prices[buy_date]
        if not prices:
            return 0
        if k >= len(prices)/2: #!!!!!!!!>= not >, or the last test case with time out
            result = 0
            for i in xrange(len(prices)-1):
                if gain(i, i+1)>0:
                    result += gain(i, i+1)
            return result
        global_max = [[0 for j in xrange(k+1)] for i in [0, 1]] # !!!!!!!need be k+1 columns, because k can be 1,2,3,..., k
        sell_max = [[0 for j in xrange(k+1)] for i in [0, 1]]
        for i in xrange(1, len(prices)):
            for j in xrange(1, k+1):
                sell_max[i%2][j] = max(sell_max[(i-1)%2][j]+gain(i-1, i), global_max[(i-1)%2][(j-1)]+gain(i-1, i)) # rolling array can only be used for row, not for col!!!!!!!!
                global_max[i%2][j] = max(global_max[(i-1)%2][j], sell_max[i%2][j])
        return global_max[(len(prices)-1)%2][k]
