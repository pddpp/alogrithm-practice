class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        # write your code here
        # Implemented myself with few defects
        if not matrix:
            return 0
        if len(matrix)==1 or len(matrix[0]) == 1: # if len == 1
            for i in xrange(len(matrix)):
                for j in xrange(len(matrix[0])):
                    if matrix[i][j] == 1:
                        return 1
            else:
                return 0
        dp = [matrix[0][:], matrix[1][:]] #!!!!!!!!not[matrix[1][:], matrix[2][:]]
        result = 0
        for i in xrange(1, len(matrix)): # !!!!!!!!!!!! not len(matrix[0]) here!!!
            dp[i%2][0] = matrix[i][0]
            for j in xrange(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i%2][j] = min(dp[(i-1)%2][j-1], dp[i%2][j-1], dp[(i-1)%2][j])+1 #updating line by line, so need a 2*len(matrix[0]) dp array
                    result = max(result, dp[i%2][j]*dp[i%2][j])
                else:
                    dp[i%2][j] = 0
        return result
