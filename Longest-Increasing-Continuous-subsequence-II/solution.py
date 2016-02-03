class Solution:
    # @param {int[][]} A an integer matrix
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequenceII(self, A):
        # Write your code here
        # classic dp search question, idea got from lecture and implemented with minor defects, need to be familiar with this solution
        def search(i, j):
            if not visited[i][j]:
                di = [1, -1, 0, 0]
                dj = [0, 0, 1, -1]
                for k in range(4):
                    ni = i+di[k]
                    nj = j+dj[k]
                    if isValid(ni, nj):
                        if A[i][j] > A[ni][nj]:
                            lics[i][j] = max(lics[i][j], search(ni, nj)+1)
            visited[i][j] = True
            return lics[i][j]
        def isValid(i, j):
            if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
                return False
            return True
        if not A or not A[0]:
            return 0
        visited = [[False for i in xrange(len(A[0]))] for j in xrange(len(A))]
        lics = [[1 for i in xrange(len(A[0]))] for j in xrange(len(A))]
        result = 1
        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                result = max(result, search(i,j)) #!! the main function of this search dp problem is very simple
        return result
